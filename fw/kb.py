import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
    )
    row_pins = (
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
    )
    data_pin = board.GP0
    # data_pin2 =
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12
    diode_orientation = DiodeOrientation.ROW2COL
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,                      41, 40, 39, 38, 37, 36,
        6,  7,  8,  9, 10, 11,                      47, 46, 45, 44, 43, 42,
        12, 13, 14, 15, 16, 17,                     53, 52, 51, 50, 49, 48,
        18, 19, 20, 21, 22, 23,                     59, 58, 57, 56, 55, 54,
                26, 27,                                     63, 62,
                        28, 29,                     65, 64,
                                34, 35,     71, 70,
                                32, 33,     69, 68
    ]