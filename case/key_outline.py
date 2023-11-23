from enum import Enum
from typing import Self, List
from cadquery import Location, Sketch, Vector
import numpy
import pykle_serial
from scipy.spatial import distance

class Direction(Enum):
    TOP = 1
    BOTTOM = 2
    RIGHT = 3
    LEFT = 4

class Key:
    def __init__(self, key:pykle_serial.Key, key_pitch: float, key_hole_size: float, draw_direction: Direction) -> None:
        self.key = key
        self.key_pitch = key_pitch
        self.key_hole_size = key_hole_size
        self.key_size_gap = self.key_hole_size - self.key_pitch
        self.direction = draw_direction

    def _rotate(self, deg, x, y, rx=0, ry=0) -> (float, float):
        rad = numpy.radians(deg) # 角度法を弧度法に変換
        xd = numpy.cos(rad) * (x - rx) + numpy.sin(rad) * (y - ry)
        yd = -numpy.sin(rad) * (x - rx) + numpy.cos(rad) * (y - ry)
        return xd + rx, yd + ry

    def _center_location(self) -> Location:
        pitch = self.key_pitch
        key = self.key

        width = pitch * key.width
        height = pitch * key.height
        angle = key.rotation_angle
        x = pitch * key.x + (width / 2)
        y = -(pitch * key.y + (height / 2))

        if angle != 0:
            rx = pitch * key.rotation_x
            ry = -(pitch * key.rotation_y)
            x, y = self._rotate(angle, x, y, rx, ry)

        return Location(Vector(x, y, 0))

    def _base_segment(self) -> (Vector, Vector):
        center = self._center_location()
        centerX, centerY, _ = center.toTuple()[0]
        gap = self.key_hole_size - self.key_pitch
        width = (self.key_pitch * self.key.width) + gap
        height = (self.key_pitch * self.key.height) + gap

        match self.direction:
            case Direction.TOP:
                startX = centerX - width / 2
                endX = centerX + width / 2
                startY = centerY + height / 2
                endY = centerY + height / 2
            case Direction.BOTTOM:
                startX = centerX + width / 2
                endX = centerX - width / 2
                startY = centerY - height / 2
                endY = centerY - height / 2
            case Direction.LEFT:
                startX = centerX - width / 2
                endX = centerX - width / 2
                startY = centerY - height / 2
                endY = centerY + height / 2
            case Direction.RIGHT:
                startX = centerX + width / 2
                endX = centerX + width / 2
                startY = centerY + height / 2
                endY = centerY - height / 2

        startPos = Vector(startX, startY)
        endPos = Vector(endX, endY)
        return (startPos, endPos)

    def segment(self, prevKey: Self, nextKey: Self) -> [(Vector, Vector)]:
        center = self._center_location()
        centerX, centerY, _ = center.toTuple()[0]
        angle = self.key.rotation_angle

        prevSegment = None
        if prevKey is not None:
            prevSegment = prevKey._base_segment()
        nextSegment = None
        if nextKey is not None:
            nextSegment = nextKey._base_segment()

        baseSegment = self._base_segment()
        gap = (self.key_hole_size - self.key_pitch) / 2

        match self.direction:
            case Direction.TOP:
                if nextKey is not None and nextKey.direction == Direction.TOP:
                    baseSegment[1].x -= gap
                if prevKey is not None and prevKey.direction == Direction.TOP:
                    baseSegment[0].x += gap
            case Direction.BOTTOM:
                if nextKey is not None and nextKey.direction == Direction.BOTTOM:
                    baseSegment[1].x += gap
                if prevKey is not None and prevKey.direction == Direction.BOTTOM:
                    baseSegment[0].x -= gap
            case Direction.LEFT:
                if nextKey is not None and nextKey.direction == Direction.LEFT:
                    baseSegment[1].y -= gap
                    if baseSegment[1].x > nextSegment[0].x:
                        baseSegment[1].y -= gap
                    else:
                        baseSegment[1].y += gap
                if prevKey is not None and prevKey.direction == Direction.LEFT:
                    baseSegment[0].y += gap
                    if baseSegment[0].x < prevSegment[1].x:
                        baseSegment[0].y -= gap
                    else:
                        baseSegment[0].y += gap
            case Direction.RIGHT:
                if nextKey is not None and nextKey.direction == Direction.RIGHT:
                    baseSegment[1].y += gap
                    if baseSegment[1].x < nextSegment[0].x:
                        baseSegment[1].y += gap
                    else:
                        baseSegment[1].y -= gap
                if prevKey is not None and prevKey.direction == Direction.RIGHT:
                    baseSegment[0].y -= gap
                    if baseSegment[0].x > prevSegment[1].x:
                        baseSegment[0].y += gap
                    else:
                        baseSegment[0].y -= gap

        startX, startY = self._rotate(angle, baseSegment[0].x, baseSegment[0].y, centerX, centerY)
        endX, endY = self._rotate(angle, baseSegment[1].x, baseSegment[1].y, centerX, centerY)
        startPos = Vector(startX, startY)
        endPos = Vector(endX, endY)
        dist = distance.euclidean([startX, startY], [endX, endY])
        return [(startPos, endPos)]

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def fromText(text: str):
        splittedText = text.split(",")
        y = int(splittedText[0])
        x = int(splittedText[1])
        return Coordinate(x, y)

    def __str__(self):
        return f"{self.y},{self.x}"

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

def coordinate(self: pykle_serial.Key) -> Coordinate:
    return Coordinate.fromText(self.labels[0])
pykle_serial.Key.coordinate = coordinate

def _to_keys_for_draw(
    self: pykle_serial.Keyboard,
    key_pitch: float,
    key_hole_size: float,
    top_left: Coordinate,
    bottom_right: Coordinate,
) -> List[Key]:
    keys: List[Key] = []

    # 上端
    topKeys = filter(lambda key: key.coordinate().y == top_left.y, self.keys)
    withInRangeKeys = filter(lambda key: top_left.x <= key.coordinate().x and key.coordinate().x <= bottom_right.x, topKeys)
    sortedKeys = sorted(withInRangeKeys, key=lambda key: key.width, reverse=True)
    sortedKeys = sorted(sortedKeys, key=lambda key: key.coordinate().x)
    sortedKeys = dict(zip(list([key.coordinate().x for key in sortedKeys]), sortedKeys)).values()

    for key in sortedKeys:
        keys.append(Key(key, key_pitch, key_hole_size, Direction.TOP))

    # 右端
    rightKeys: List[Key] = []
    for y in range(top_left.y, bottom_right.y + 1):
        lineKeys = filter(lambda key: key.coordinate().y == y, self.keys)
        withInRangeKeys = filter(lambda key: top_left.x <= key.coordinate().x and key.coordinate().x <= bottom_right.x, lineKeys)
        rightKeys.append(max(list(withInRangeKeys), key=lambda item: item.coordinate().x))

    sortedKeys = sorted(rightKeys, key=lambda key: key.width, reverse=True)
    sortedKeys = sorted(sortedKeys, key=lambda key: key.coordinate().y)
    sortedKeys = dict(zip(list([key.coordinate().y for key in sortedKeys]), sortedKeys)).values()

    for key in sortedKeys:
        keys.append(Key(key, key_pitch, key_hole_size, Direction.RIGHT))

    # 下端
    topKeys = filter(lambda key: key.coordinate().y == bottom_right.y, self.keys)
    withInRangeKeys = filter(lambda key: top_left.x <= key.coordinate().x and key.coordinate().x <= bottom_right.x, topKeys)
    sortedKeys = sorted(withInRangeKeys, key=lambda key: key.width, reverse=True)
    sortedKeys = sorted(sortedKeys, key=lambda key: key.coordinate().x, reverse=True)
    sortedKeys = dict(zip(list([key.coordinate().x for key in sortedKeys]), sortedKeys)).values()

    for key in sortedKeys:
        keys.append(Key(key, key_pitch, key_hole_size, Direction.BOTTOM))

    # 左端
    leftKeys: List[Key] = []
    for y in range(top_left.y, bottom_right.y + 1):
        lineKeys = filter(lambda key: key.coordinate().y == y, self.keys)
        withInRangeKeys = filter(lambda key: top_left.x <= key.coordinate().x and key.coordinate().x <= bottom_right.x, lineKeys)
        leftKeys.append(min(list(withInRangeKeys), key=lambda item: item.coordinate().x))
    sortedKeys = sorted(leftKeys, key=lambda key: key.width, reverse=True)
    sortedKeys = sorted(sortedKeys, key=lambda key: key.coordinate().y, reverse=True)
    sortedKeys = dict(zip(list([key.coordinate().y for key in sortedKeys]), sortedKeys)).values()

    for key in sortedKeys:
        keys.append(Key(key, key_pitch, key_hole_size, Direction.LEFT))

    return keys
pykle_serial.Keyboard._to_keys_for_draw = _to_keys_for_draw

class KeyOutlineDrawer:
    MINIMUM_LENGTH = 1.0
    EXTENSION_UNIT = 0.05

    def __init__(self, kle_json_path: str, key_pitch: float, key_hole_size: float):
        json_file = open(kle_json_path, 'r')
        json_text = json_file.read()
        keyboard = pykle_serial.serial.parse(json_text)

        self.keyboard = keyboard
        self.key_pitch = key_pitch
        self.key_hole_size = key_hole_size

    def draw_key_outline(
        self,
        *areas: (Coordinate, Coordinate)
    ) -> Sketch:
        sketch = Sketch()
        for top_left, bottom_right in areas:
            self._draw_part_of_key_outline(sketch, top_left, bottom_right)
        sketch.assemble()

        # センター出し
        min_x = sketch.vertices("<X").val().toTuple()[0]
        sketch.reset()
        max_x = sketch.vertices(">X").val().toTuple()[0]
        sketch.reset()
        width = distance.euclidean([min_x, 0], [max_x, 0])
        min_y = sketch.vertices("<Y").val().toTuple()[1]
        sketch.reset()
        max_y = sketch.vertices(">Y").val().toTuple()[1]
        sketch.reset()
        height = distance.euclidean([0, min_y], [0, max_y])

        return sketch.moved(Location((-width / 2 - min_x, -height / 2 - min_y, 0)))

    def _draw_part_of_key_outline(
        self,
        sketch: Sketch,
        top_left: Coordinate,
        bottom_right: Coordinate
    ) -> Sketch:
        keys = self.keyboard._to_keys_for_draw(self.key_pitch, self.key_hole_size, top_left, bottom_right)

        segments = []
        # 外周segmentを生成
        for index in range(0, len(keys)):
            prevKey: Key = None
            if index > 0:
                prevKey = keys[index - 1]
            key: Key = keys[index]
            nextKey: Key = None
            if index < len(keys) - 1:
                nextKey = keys[index + 1]

            pos = key.segment(prevKey, nextKey)
            segments+=(pos)

        # 生成した外周segmentを調整その1
        for index, segment in enumerate(segments):
            nextSegment = None
            if len(segments) > index + 1:
                nextSegment = segments[index + 1]

            # segmentが交差する場合は交点でつながるようにする
            if nextSegment is not None:
                crossPoint = self._calc_cross_point(segment[0].toTuple(), segment[1].toTuple(), nextSegment[0].toTuple(), nextSegment[1].toTuple())
                if crossPoint[0] is True:
                    segments[index] = (segment[0], Vector(crossPoint[1][0], crossPoint[1][1]))
                    segments[index + 1] = (Vector(crossPoint[1][0], crossPoint[1][1]), nextSegment[1])

        # 生成した外周segmentを調整その2
        for index, segment in enumerate(segments):
            nextSegment = None
            if len(segments) > index + 1:
                nextSegment = segments[index + 1]

            # 最低長さ以下のsegmentを延長
            # 現状はX方向に伸ばすだけなので汎用では使えません
            # TODO うまいこと延長するように修正する
            if nextSegment is not None and segment[1] != nextSegment[0]:
                startPos = [segment[1].x, segment[1].y]
                endPos = [nextSegment[0].x, nextSegment[0].y]
                dist = distance.euclidean(startPos, endPos)
                while dist < self.MINIMUM_LENGTH:
                    newX = endPos[0] + self.EXTENSION_UNIT
                    endPos = [newX, endPos[1]]
                    dist = distance.euclidean(startPos, endPos)
                segments[index + 1] = (Vector(endPos[0], endPos[1]), nextSegment[1])

        # 生成したsegmentをSketchに描画
        for index, segment in enumerate(segments):
            nextSegment = None
            if len(segments) > index + 1:
                nextSegment = segments[index + 1]

            sketch.segment(segment[0], segment[1])
            if nextSegment is not None and segment[1] != nextSegment[0]:
                # 隙間があれば直線で接続
                sketch.segment(segment[1], nextSegment[0])

        return sketch

    def _calc_cross_point(self, point_a, point_b, point_c, point_d):
        cross_point = (0,0)
        denom = (point_b[0] - point_a[0]) * (point_d[1] - point_c[1]) - (point_b[1] - point_a[1]) * (point_d[0] - point_c[0])

        # 直線が平行な場合
        if (round(denom) <= 0):
            return False, cross_point

        vector_a_to_c = ((point_c[0] - point_a[0]), (point_c[1] - point_a[1]))
        r = ((point_d[1] - point_c[1]) * vector_a_to_c[0] - (point_d[0] - point_c[0]) * vector_a_to_c[1]) / denom

        distance = ((point_b[0] - point_a[0]) * r, (point_b[1] - point_a[1]) * r)
        cross_point = (point_a[0] + distance[0], point_a[1] + distance[1])

        return True, cross_point
