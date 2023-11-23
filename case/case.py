from cadquery import Workplane, Sketch, Location, exporters
from cqkit import export_step_file
import numpy
import daughter_board
from key_outline import KeyOutlineDrawer, Coordinate
import sketch_extensions

#from jupyter_cadquery.viewer.client import show

# ケース角度
TYPING_ANGLE = 6.0

# ケース四隅フィレット
CASE_CORNER_R = 10.0

# ケース面取り
CASE_CHAMFER_D = 1.0

# スイッチプレート寸法
SWITCH_PLATE_TAB_LENGTH = 2.0
SWITCH_PLATE_WIDTH = 286.9875
SWITCH_PLATE_HEIGHT = 97.9854
SWITCH_PLATE_THICKNESS = 1.6

# スイップレート寸法からケース上面寸法を計算
CASE_TOP_FRAME = 4.0
CASE_MARGIN_SWITCH_PLATE = 1.0
CASE_TOP_WIDTH = SWITCH_PLATE_WIDTH + (CASE_TOP_FRAME + CASE_MARGIN_SWITCH_PLATE) * 2
CASE_TOP_HEIGHT = SWITCH_PLATE_HEIGHT + (CASE_TOP_FRAME + CASE_MARGIN_SWITCH_PLATE) * 2

# ケース上面寸法からケース下面寸法を計算
CASE_BOTTOM_SIZE_OFFSET = 10.0
CASE_BOTTOM_WIDTH = CASE_TOP_WIDTH +  CASE_BOTTOM_SIZE_OFFSET
CASE_BOTTOM_HEIGHT = CASE_TOP_HEIGHT +  CASE_BOTTOM_SIZE_OFFSET

# ベースプレート寸法
CASE_BOTTOM_FRAME = 4.0
BASE_PLATE_WIDTH = CASE_BOTTOM_WIDTH - CASE_BOTTOM_FRAME * 2
BASE_PLATE_HEIGHT = CASE_BOTTOM_HEIGHT - CASE_BOTTOM_FRAME * 2
BASE_PLATE_CORNER_R = CASE_CORNER_R - CASE_BOTTOM_FRAME
BASE_PLATE_THICKNESS = 5

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
BASE_PLATE_TOP_TO_DAUGHTER_BOARD_TOP = 7.5
BOARD_MARGIN = 1.0

# キーレイアウト関連定義
KLE_JSON_PATH = "../layout/yak40.json"
KEY_PITCH = 19.05
KEY_HOLE_SIZE = 20

KEY_OFFSET = 2.5

KEY_OUTLINE_INSIDE_CORNER_R = 0.6
KEY_OUTLINE_OUTSIDE_CORNER_R = 1.5

#=====================================
# メインブロック
#=====================================
main_body = (
    Workplane("XY")
    .rect(CASE_BOTTOM_WIDTH, CASE_BOTTOM_HEIGHT)
    .transformed(
        offset=(0, 0, CASE_HEIGHT + (numpy.tan(numpy.radians(TYPING_ANGLE)) * CASE_TOP_HEIGHT) / 2),
        rotate=(TYPING_ANGLE, 0, 0)
    )
    .rect(CASE_TOP_WIDTH, CASE_TOP_HEIGHT)
    .loft(combine=True)
    .edges(">>Y[1] or <<Y[1]")
    .fillet(CASE_CORNER_R)
)

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
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_LEFT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE + 10),
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_LEFT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE),
    (-SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_CENTER_TO_LEFT, SWITCH_PLATE_HEIGHT / 2 - SWITCH_PLATE_TOP_TO_INNER_TOP + CASE_MARGIN_SWITCH_PLATE + SWITCH_PLATE_TAB_LENGTH),
    (SWITCH_PLATE_WIDTH / 2 - SWITCH_PLATE_RIGHT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE),
    (SWITCH_PLATE_WIDTH / 2 - SWITCH_PLATE_RIGHT_SIDE_WIDTH, SWITCH_PLATE_HEIGHT / 2 + CASE_MARGIN_SWITCH_PLATE + 10),
]
components_outline_sketch = (
    Sketch()
    .rect(
        SWITCH_PLATE_WIDTH + CASE_MARGIN_SWITCH_PLATE * 2,
        SWITCH_PLATE_HEIGHT + CASE_MARGIN_SWITCH_PLATE
    )
    .polygon(points, mode="s")
    .vertices()
    .fillet(BASE_PLATE_CORNER_R)
)

#=====================================
# キー外形のスケッチを作成
#=====================================
key_outline_sketch: Sketch = (
    KeyOutlineDrawer(KLE_JSON_PATH, KEY_PITCH, KEY_HOLE_SIZE)
    .draw_key_outline(
        (Coordinate(0, 0), Coordinate(5, 3)),
        (Coordinate(6, 0), Coordinate(12, 3))
    )
    .outside_vertices()
    .fillet(KEY_OUTLINE_OUTSIDE_CORNER_R)
    .reset()
    .inside_vertices()
    .fillet(KEY_OUTLINE_INSIDE_CORNER_R)
)

#=====================================
# ドーターボードスペース用オブジェクトを作成
#=====================================
daughter_board_mold = daughter_board.make_daughter_board_male_mold()
daughter_board_mold = daughter_board_mold.translate(
    (
        # USB中心とキー配置中央が一致するように移動
        -SWITCH_PLATE_WIDTH / 2 + SWITCH_PLATE_CENTER_TO_LEFT + daughter_board.BOARD_CENTER_TO_USB_CENTER,
        CASE_BOTTOM_HEIGHT / 2 - CASE_BOTTOM_FRAME - daughter_board.MAX_BOARD_HEIGHT / 2 - BOARD_MARGIN,
        BASE_PLATE_THICKNESS + BASE_PLATE_TOP_TO_DAUGHTER_BOARD_TOP
    )
)

#=====================================
# 組み立て
#=====================================
result = (
    main_body
    .faces(">Z")
    .tag("case_top")
    # キー外形の穴を開ける
    .placeSketch(key_outline_sketch.moved(Location((0, -KEY_OFFSET, 0))))
    .cutThruAll()
    # スイッチプレート/PCBが収まるように切り取り
    .faces(tag="case_top")
    .workplane(offset=-CASE_TOP_TO_SWITCH_PLATE_TOP)
    .placeSketch(components_outline_sketch.moved(Location((0, -KEY_OFFSET, 0))))
    .cutBlind(main_body.faces("<Z").val())
    # キー外形の縁を面取り
    .edges(">X[1] or <X[1]")
    .edges(">Z")
    .chamfer(0.5)
    # ボディ上面/下面エッジを面取り
    .faces(tag="case_top")
    .edges()
    .chamfer(CASE_CHAMFER_D)
    .faces("<Z")
    .edges()
    .chamfer(CASE_CHAMFER_D)
    # ベースプレートを切り取り
    .cut(base_plate)
    # ドーターボード部分切り取り
    .cut(daughter_board_mold)
)
export_step_file(result, "./case.step", title="A case of The Yak40 keyboard", author="kurikisasa")

#show(result)
