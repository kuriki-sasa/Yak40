from cadquery import Workplane
import numpy
import sketch_extensions

# 貫通に十分な長さ
THROUGH_LENGTH = 50.0

# UDBからボディまでのマージン
MARGIN = 0.5

# UDB-Sの寸法
BOARD_WIDTH = 40.0
BOARD_HEIGHT = 9.0
BOARD_THICK = 1.6
MOUNTING_HOLE_INTERVAL = 33.0

# UDBから飛び出したUSB部分のクリアランス寸法
USB_CLEARANCE_CORNER_R = 2.0
USB_CLEARANCE_WIDTH = 12.6
USB_CLEARANCE_HEIGHT = 1.3

# USB穴寸法
USB_HOLE_WIDE = 9.35
USB_HOLE_THICK = 3.56
USB_HOLE_CORNER_R = 1.5

# USBコネクタのシェルを避けるためのカットアウト寸法
USB_SHELL_CUTOUT_WIDTH = 15.2
USB_SHELL_CUTOUT_HEIGHT = 9.0
USB_SHELL_CUTOUT_OFFSET = 1
USB_SHELL_CUTOUT_CORNER_R = 3.5

# ケーブル経路の寸法
CABLE_TRENCH_WIDE = 8.5

# UDBをケースに接触させないためのエアギャップ
MOUNTING_HOLE_MARGIN_R = 2.875
MOUNTING_HOLE_MARGIN_SMOOTHING_R = 2
# エアギャップの高さはUDB推奨の0.5mm
AIR_GAP_HEIGHT = 0.5

# UDB基準の相対位置
BOARD_CENTER_TO_USB_CENTER = 7.6
BOARD_CENTER_TO_TRENCH_CENTER = 9.5
BOARD_BOTTOM_TO_USB_CENTER = BOARD_THICK + 3.26 / 2

# CNCで加工できるようにフィレットするためのR
MALE_MOLD_R = 2.0

# マージンを考慮した
MAX_BOARD_HEIGHT = BOARD_HEIGHT + MARGIN / 2 + USB_CLEARANCE_HEIGHT + MARGIN

def make_daughter_board_male_mold() -> Workplane:
    # UDB基板部分
    board = (
        Workplane("XY")
        .slot2D(
            BOARD_WIDTH + MARGIN,
            BOARD_HEIGHT + MARGIN
        )
        .extrude(-THROUGH_LENGTH)
    )

    # UDBのUSB部分の出っ張り
    usb_clearance_face = (
        Workplane("XY")
        .sketch()
        .center(-BOARD_CENTER_TO_USB_CENTER, BOARD_HEIGHT / 2)
        .rect(USB_CLEARANCE_WIDTH, (USB_CLEARANCE_HEIGHT + MARGIN) * 2)
        .reset()
        # CNCで加工できるように角をフィレット
        .vertices(">Y")
        .fillet(USB_CLEARANCE_CORNER_R)
        .finalize()
    )
    usb_clearance = (
        usb_clearance_face
        .extrude(-THROUGH_LENGTH)
    )

    # ケーブル経路
    cable_trench_face = (
        Workplane("XY")
        .sketch()
        .center(BOARD_CENTER_TO_TRENCH_CENTER, -(BOARD_HEIGHT + THROUGH_LENGTH) / 2 + (BOARD_HEIGHT / 4)) # 綺麗じゃないけど余裕をもって接続
        .rect(CABLE_TRENCH_WIDE, THROUGH_LENGTH)
        .finalize()
    )
    cable_trench = (
        cable_trench_face
        .extrude(-THROUGH_LENGTH)
    )

    # 結合
    main_mold = board + usb_clearance + cable_trench
    # CNCで加工できるように角をフィレット
    main_mold = main_mold.edges("|Z").fillet(MALE_MOLD_R)

    # 短絡を防ぐためにUDBとケースの間にエアギャップを設ける
    # CNCで加工できるように、ねじ部から外壁へスムーズに接続するための接点を計算する
    mounting_hole_to_smoothing_r_center = numpy.sqrt(numpy.power(MOUNTING_HOLE_MARGIN_R + MOUNTING_HOLE_MARGIN_SMOOTHING_R, 2) - numpy.power((BOARD_HEIGHT + MARGIN) / 2 - MOUNTING_HOLE_MARGIN_SMOOTHING_R , 2))
    mounting_hole_to_smoothing_radians = numpy.arcsin(((BOARD_HEIGHT + MARGIN) / 2 - 2) / (MOUNTING_HOLE_MARGIN_R + 2))
    mounting_hole_to_smoothing = MOUNTING_HOLE_MARGIN_R * numpy.cos(mounting_hole_to_smoothing_radians)

    air_gap = (
        Workplane()
        .sketch()
        # スムーズに接続するための部分を描画
        .rect(MOUNTING_HOLE_INTERVAL - mounting_hole_to_smoothing * 2, MOUNTING_HOLE_MARGIN_R * 2)
        .center(0, (BOARD_HEIGHT + MARGIN) / 2 - 2)
        .slot(MOUNTING_HOLE_INTERVAL - mounting_hole_to_smoothing_r_center * 2, 4)
        .reset()
        .center(0, -((BOARD_HEIGHT + MARGIN) / 2 - 2))
        .slot(MOUNTING_HOLE_INTERVAL - mounting_hole_to_smoothing_r_center * 2, 4)
        .reset()
        # ねじ部を切り取り
        .center(MOUNTING_HOLE_INTERVAL / 2, 0)
        .circle(MOUNTING_HOLE_MARGIN_R, mode="s")
        .reset()
        .center(-MOUNTING_HOLE_INTERVAL / 2, 0)
        .circle(MOUNTING_HOLE_MARGIN_R, mode="s")
        .reset()
        .finalize()
        .extrude(AIR_GAP_HEIGHT)
    )
    # エアギャップ上端に揃えるためにUSBクリアランス/ケーブル通路を押し出し
    usb_clearance_to_top = (
        usb_clearance_face
        .extrude(AIR_GAP_HEIGHT)
    )
    cable_trench_to_top = (
        cable_trench_face
        .extrude(AIR_GAP_HEIGHT)
    )
    air_gap = (air_gap + usb_clearance_to_top + cable_trench_to_top).edges("|Z").fillet(MALE_MOLD_R)

    # USB差し込み口
    usb_hole = (
        Workplane("XZ")
        .center(-BOARD_CENTER_TO_USB_CENTER, -BOARD_BOTTOM_TO_USB_CENTER)
        .rect(USB_HOLE_WIDE, USB_HOLE_THICK)
        .extrude(-THROUGH_LENGTH)
        .edges("|Y")
        .fillet(USB_HOLE_CORNER_R)
    )
    # USBコネクターのシェルカットアウト
    usb_shell_cutout = (
        usb_hole
        .faces("<Y")
        .workplane(offset=-((BOARD_HEIGHT + MARGIN) / 2 + USB_CLEARANCE_HEIGHT + MARGIN + USB_SHELL_CUTOUT_OFFSET))
        .rect(USB_SHELL_CUTOUT_WIDTH, USB_SHELL_CUTOUT_HEIGHT)
        .extrude(-THROUGH_LENGTH)
        .edges("|Y")
        .fillet(USB_SHELL_CUTOUT_CORNER_R)
    )

    return main_mold + usb_hole + usb_shell_cutout + air_gap
