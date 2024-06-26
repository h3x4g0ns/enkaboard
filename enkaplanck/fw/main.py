import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = _KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.COL1, board.COL2, board.COL3, board.COL4, board.COL5, board.COL6, 
    board.COL7, board.COL8, board.COL9, board.COL10, board.COL11, board.COL12,
)
keyboard.row_pins = (
    board.ROW1, board.ROW2, board.ROW3, board.ROW4,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FN = KC.MO(1)
XXXXXXX = KC.TRNS

keyboard.keymap = [
    [
        KC.GESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQUAL, KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,  KC.BSLASH,
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, XXXXXXX,  KC.ENTER,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX, XXXXXXX,  KC.RSFT,
        KC.LCTRL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.RGUI, FN,      XXXXXXX,  KC.RCTRL
    ],
    [
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,    KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,   KC.F12,  KC.DEL,
        XXXXXXX, XXXXXXX, KC.UP,   XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.INS,  KC.HOME, KC.PGUP, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.DEL,  KC.END,  KC.PGDN, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, KC.MUTE, KC.VOLD, KC.VOLU, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.APP,  XXXXXXX,  XXXXXXX, XXXXXXX,
    ],
]

if __name__ == '__main__':
    keyboard.go()
