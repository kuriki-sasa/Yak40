from cadquery import Vector, Workplane, Sketch, Location
from cqkit import export_step_file, export_stl_file
import numpy
import daughter_board
from key_outline import KeyOutlineDrawer, Coordinate
from yak40_selectors import AngledFaceSelector
import sketch_extensions
import workplane_extensions

# from jupyter_cadquery.viewer.client import show

# ケース角度
TYPING_ANGLE = 6.0

# ケース四隅フィレット
CASE_CORNER_R = 9.0

# ケース面取り
CASE_TOP_FILLET_R = 0.8
CASE_BOTTOM_FILLET_R = CASE_TOP_FILLET_R
KEY_HOLE_CHAMFER_D = 0.5

# スイッチプレート寸法
SWITCH_PLATE_TAB_LENGTH = 2.0
SWITCH_PLATE_WIDTH = 286.9875
SWITCH_PLATE_HEIGHT = 97.9854
SWITCH_PLATE_THICKNESS = 1.6

# スイップレート寸法からケース上面寸法を計算
CASE_TOP_FRAME = 4.0
CASE_MARGIN_SWITCH_PLATE = 1.0
CASE_TOP_OFFSET = -1.8
CASE_TOP_WIDTH = SWITCH_PLATE_WIDTH + (CASE_TOP_FRAME + CASE_MARGIN_SWITCH_PLATE) * 2
CASE_TOP_HEIGHT = SWITCH_PLATE_HEIGHT + (CASE_TOP_FRAME + CASE_MARGIN_SWITCH_PLATE) * 2

# ケース上面寸法からケース下面寸法を計算
CASE_BOTTOM_WIDTH_OFFSET = 10.0
CASE_BOTTOM_HEIGHT_OFFSET = 16.0
CASE_BOTTOM_WIDTH = CASE_TOP_WIDTH +  CASE_BOTTOM_WIDTH_OFFSET
CASE_BOTTOM_HEIGHT = CASE_TOP_HEIGHT +  CASE_BOTTOM_HEIGHT_OFFSET

# ベースプレート寸法
CASE_BOTTOM_FRAME = 4.0
BASE_PLATE_WIDTH = CASE_BOTTOM_WIDTH - CASE_BOTTOM_FRAME * 2
BASE_PLATE_HEIGHT = CASE_BOTTOM_HEIGHT - CASE_BOTTOM_FRAME * 2
BASE_PLATE_CORNER_R = CASE_CORNER_R - CASE_BOTTOM_FRAME
BASE_PLATE_THICKNESS = 5.0
BASE_PLATE_SCREW_OFFSET = 5.0

# 各種高さ寸法
CASE_TOP_TO_SWITCH_PLATE_TOP =  7.0
SWITCH_PLATE_BOTTOM_TO_PCB_TOP = 3.5
PCB_THICKNESS = 1.6
MAX_BOARD_COMPONENT_THICKNESS = 2.5
MAIN_COMPONENTS_THICKNESS = SWITCH_PLATE_THICKNESS + SWITCH_PLATE_BOTTOM_TO_PCB_TOP + PCB_THICKNESS + MAX_BOARD_COMPONENT_THICKNESS

# ケース高さ
CASE_HEIGHT_MARGIN = 2.0
CASE_HEIGHT = CASE_TOP_TO_SWITCH_PLATE_TOP + MAIN_COMPONENTS_THICKNESS + BASE_PLATE_THICKNESS + CASE_HEIGHT_MARGIN

# ドーターボード配置用寸法
BASE_PLATE_TOP_TO_DAUGHTER_BOARD_TOP = 9.0
BOARD_MARGIN = 4.5

# ねじ穴
M3_HOLE_DIAMETER = 2.5
M3_TAPPING_MARGIN = M3_HOLE_DIAMETER / 2.0
M3_HOLE_DEPTH = 5 + M3_TAPPING_MARGIN
M2_HOLE_DIAMETER = 1.6
M2_TAPPING_MARGIN = M2_HOLE_DIAMETER / 2.0
M2_HOLE_DEPTH = 3 + M2_TAPPING_MARGIN

# Oリングバーガーマウント用寸法
O_RING_DENT_DIA = 4.3
O_RING_DENT_DEPTH = 0.3

# キーレイアウト関連定義
KLE_JSON_PATH = "../layout/yak40.json"
KEY_PITCH = 19.05
KEY_HOLE_SIZE = 20

# Alice配列である都合、単純に高さの半分 = キーレイアウトの中心でないのでずらす
KEYS_CENTER_TO_PLATE_SWITCH_PLATE_CENTER = 0.71775
KEYS_OFFSET = 0.0

KEYS_OUTLINE_INSIDE_CORNER_R = 0.6
KEYS_OUTLINE_OUTSIDE_CORNER_R = 1.5

#=====================================
# メインブロック
#=====================================
case_bottom_sketch = (
    Sketch()
    .rect(CASE_BOTTOM_WIDTH, CASE_BOTTOM_HEIGHT)
    .vertices()
    .fillet(CASE_CORNER_R)
)
case_top_sketch = (
    Sketch()
    .rect(CASE_TOP_WIDTH, CASE_TOP_HEIGHT)
    .vertices()
    .fillet(CASE_CORNER_R)
    .rotate((0, 0, 0), (1, 0, 0), TYPING_ANGLE)
    .moved(Location((0, CASE_TOP_OFFSET, CASE_HEIGHT + (numpy.tan(numpy.radians(TYPING_ANGLE)) * CASE_TOP_HEIGHT) / 2)))
)

main_body = (
    Workplane("XY")
    .placeSketch(case_bottom_sketch, case_top_sketch)
    .loft(combine=True)
    # ボディ上面/下面エッジを面取り
    .faces(">Z")
    .edges()
    .fillet(CASE_TOP_FILLET_R)
    .faces("<Z")
    .edges()
    .fillet(CASE_BOTTOM_FILLET_R)
)

#=====================================
# PCB、スイッチプレートを収めるための外形
#=====================================
# スイッチプレート中央部のへこみのための寸法
SWITCH_PLATE_LEFT_SIDE_WIDTH = 57.5314
SWITCH_PLATE_RIGHT_SIDE_WIDTH = 67.0594
SWITCH_PLATE_TOP_TO_INNER_TOP = 16.1636
SWITCH_PLATE_CENTER_TO_LEFT = 138.7313
SWITCH_PLATE_CENTER_TO_RIGHT = SWITCH_PLATE_WIDTH - SWITCH_PLATE_CENTER_TO_LEFT
points = [
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_LEFT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE + 10), # 10は切り抜きのための適当な数字
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_LEFT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE),
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_CENTER_TO_LEFT, SWITCH_PLATE_HEIGHT / 2 - SWITCH_PLATE_TOP_TO_INNER_TOP + CASE_MARGIN_SWITCH_PLATE + SWITCH_PLATE_TAB_LENGTH),
    (SWITCH_PLATE_WIDTH / 2 - SWITCH_PLATE_RIGHT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE),
    (SWITCH_PLATE_WIDTH / 2 - SWITCH_PLATE_RIGHT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE + 10), # 10は切り抜きのための適当な数字
]
components_outline_sketch = (
    Sketch()
    .rect(
        SWITCH_PLATE_WIDTH + CASE_MARGIN_SWITCH_PLATE * 2,
        SWITCH_PLATE_HEIGHT + CASE_MARGIN_SWITCH_PLATE * 2
    )
    .polygon(points, mode="s")
    .vertices()
    .fillet(BASE_PLATE_CORNER_R)
)
SWITCH_PLATE_SCREW_POINTS = [
    (114.776228, 47.692713),
    (35.342628, 38.778913),
    (-35.198172, 40.432813),
    (-97.726272, 47.693113),
    (-102.950772, -36.288187),
    (-35.644772, -44.378487),
    (45.169828, -44.377787),
    (112.476228, -36.288487)
]

#=====================================
# ベースプレート
#=====================================
base_plate = (
    Workplane()
    .rect(BASE_PLATE_WIDTH, BASE_PLATE_HEIGHT)
    .extrude(BASE_PLATE_THICKNESS)
    .edges("|Z")
    .fillet(BASE_PLATE_CORNER_R)
)
BASE_PLATE_SCREW_POINTS = [
    (0, BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET),
    (-BASE_PLATE_WIDTH / 6, -(BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
    (BASE_PLATE_WIDTH / 6, -(BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
    (-(BASE_PLATE_WIDTH / 2 - 5), -(BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
    ((BASE_PLATE_WIDTH / 2 - 5), -(BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
    (-(BASE_PLATE_WIDTH / 2 - 5), (BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
    ((BASE_PLATE_WIDTH / 2 - 5), (BASE_PLATE_HEIGHT / 2 - BASE_PLATE_SCREW_OFFSET)),
]

#=====================================
# キー外形のスケッチを作成
#=====================================
keys_outline_sketch: Sketch = (
    KeyOutlineDrawer(KLE_JSON_PATH, KEY_PITCH, KEY_HOLE_SIZE)
    .draw_key_outline(
        (Coordinate(0, 0), Coordinate(5, 3)),
        (Coordinate(6, 0), Coordinate(12, 3))
    )
    .outside_vertices()
    .fillet(KEYS_OUTLINE_OUTSIDE_CORNER_R)
    .reset()
    .inside_vertices()
    .fillet(KEYS_OUTLINE_INSIDE_CORNER_R)
    # Alice配列である都合、単純に高さの半分 = キーレイアウトの中心でないのでずらす
    .moved(Location((0, -KEYS_CENTER_TO_PLATE_SWITCH_PLATE_CENTER, 0)))
)

#=====================================
# ドーターボードスペース用オブジェクトを作成
#=====================================
daughter_board_mold = daughter_board.make_daughter_board_male_mold()
daughter_board_center = Vector(
    -SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_CENTER_TO_LEFT + daughter_board.BOARD_CENTER_TO_USB_CENTER,
    CASE_BOTTOM_HEIGHT / 2 - CASE_BOTTOM_FRAME - daughter_board.BOARD_HEIGHT / 2 - BOARD_MARGIN,
    BASE_PLATE_THICKNESS + BASE_PLATE_TOP_TO_DAUGHTER_BOARD_TOP
)
daughter_board_mold = daughter_board_mold.translate(daughter_board_center)
DAUGHTER_BOARD_SCREW_POINTS = [
    (daughter_board_center.x - daughter_board.MOUNTING_HOLE_INTERVAL / 2, -daughter_board_center.y),
    (daughter_board_center.x + daughter_board.MOUNTING_HOLE_INTERVAL / 2, -daughter_board_center.y)
]


#=====================================
# 組み立て
#=====================================
result = (
    main_body
    .faces(AngledFaceSelector(TYPING_ANGLE))
    .faces(">Z")
    .tag("case_top")
    .workplane(centerOption="CenterOfBoundBox")
    # キー外形の穴を開ける
    .placeSketch(keys_outline_sketch.moved(Location((0, -KEYS_OFFSET, 0))))
    .cutThruAll()
    # キー外形の縁を面取り
    .edges(">X[1] or <X[1]")
    .edges(">Z")
    .chamfer(KEY_HOLE_CHAMFER_D)
    # スイッチプレート/PCBが収まるように切り取り
    .faces(tag="case_top")
    .workplane(offset=-CASE_TOP_TO_SWITCH_PLATE_TOP, centerOption="CenterOfBoundBox")
    .placeSketch(components_outline_sketch.moved(Location((0, -KEYS_OFFSET, 0))))
    .cutBlind(main_body.faces("<Z").val())
    # ベースプレートを切り取り
    .cut(base_plate)
    # ベースプレート固定ねじ穴を開ける
    .faces("<Z[-2]")
    .workplane(origin=(0, 0))
    .pushPoints(BASE_PLATE_SCREW_POINTS)
    .drillHole(M3_HOLE_DIAMETER, M3_HOLE_DEPTH)
    # ドーターボード部分切り取り
    .cut(daughter_board_mold)
    # ドーターボードねじ穴開け
    .faces("<Z[2]")
    .workplane(origin=(0, 0))
    .pushPoints(DAUGHTER_BOARD_SCREW_POINTS)
    .drillHole(M3_HOLE_DIAMETER, M3_HOLE_DEPTH)
    # スイッチプレートねじ穴開け
    .faces(AngledFaceSelector(TYPING_ANGLE))
    .faces("<Z")
    .workplane(centerOption="CenterOfBoundBox")
    .pushPoints(SWITCH_PLATE_SCREW_POINTS)
    .drillHole(M2_HOLE_DIAMETER, M2_HOLE_DEPTH)
    # oリングバーガーマウント用にくぼみを掘る
    .pushPoints(SWITCH_PLATE_SCREW_POINTS)
    .hole(O_RING_DENT_DIA, O_RING_DENT_DEPTH)
)


export_step_file(result, "./build/case.step", title="A case of The Yak40 keyboard", author="kurikisasa")
export_stl_file(result, "./build/case.stl")

# show(result)
