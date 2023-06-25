from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

split = Split(
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    split_type=SplitType.UART,
    split_side=SplitSide.LEFT,
    use_pio=True,
    uart_flip = True
)

keyboard.modules.append(split)

keyboard.keymap = [
    [   #0
        KC.ESC,  KC.N1,    KC.N2,   KC.N3, KC.N4, KC.N5,                             KC.N6, KC.N7,   KC.N8,  KC.N9,   KC.N0, KC.BSPC,
        KC.GRV,   KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,                              KC.Y,  KC.U,    KC.I,   KC.O,    KC.P, KC.BSLS,
        KC.TAB,  KC.A,    KC.S,    KC.D,  KC.F,  KC.G,                              KC.H,  KC.J,    KC.K,   KC.L, KC.SCLN, KC.QUOT,
        KC.CAPS,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,                              KC.N,  KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
                        KC.LBRC, KC.RBRC,                                                           KC.MINS, KC.EQL,
                                            KC.LGUI,  KC.LSFT,          KC.SPC,     KC.ENT,
                                            KC.LCTL,  KC.LALT,          KC.UP,  KC.RIGHT,
                                            KC.MO(1), KC.DEL,           KC.LEFT,  KC.DOWN
    ],
    [  #1
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5, KC.F6,                           KC.F7, KC.F8, KC.F9,  KC.F10,  KC.F11,  KC.F12,
        KC.TRNS, KC.NO, KC.VOLU, KC.PGUP,   KC.NO, KC.NO,                         KC.NLCK, KC.P7, KC.P8,   KC.P9, KC.PMNS,   KC.NO,
        KC.TRNS, KC.NO, KC.MUTE, KC.SLCK, KC.MPLY, KC.NO,                         KC.PAST, KC.P4, KC.P5,   KC.P6, KC.PPLS, KC.TRNS,
        KC.TRNS, KC.NO, KC.VOLD, KC.PGDN,   KC.NO, KC.NO,                         KC.PSLS, KC.P1, KC.P2,   KC.P3, KC.PENT, KC.TRNS,
                          KC.NO,   KC.NO,                                                         KC.P0, KC.PDOT,
                                                 KC.TRNS, KC.TRNS,       KC.TRNS,   KC.NO,
                                                 KC.TRNS, KC.TRNS,       KC.TRNS, KC.TRNS,
                                                 KC.TRNS, KC.TRNS,       KC.TRNS, KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()