import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner, KeysScanner
from kmk.scanners.combined import CombinedScanner
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(Macros())

# 1. Matrix Setup (GP1, 2, 4 are Columns | GP28, 27, 26 are Rows)
matrix_scanner = MatrixScanner(
    column_pins=(board.GP1, board.GP2, board.GP4),
    row_pins=(board.GP28, board.GP27, board.GP26),
    columns_to_anodes=DiodeOrientation.COL2ROW,
)

# 2. Channel Buttons (GP6, 29, 7 connected to 3.3V)
direct_scanner = KeysScanner(
    pins=(board.GP6, board.GP29, board.GP7),
    value_when_pressed=True, 
    pull=True, # Uses internal pull-down to handle 3.3V logic
)

# Combine scanners into one layout
keyboard.matrix = CombinedScanner(scanners=[matrix_scanner, direct_scanner])

# 3. Macro Definitions
# Opens Run (Win+R), waits 250ms, types URL, presses Enter
YT = KC.MACRO(KC.LGUI(KC.R), KC.MW_WAIT(250), "https://youtube.com", KC.ENTER)
IG = KC.MACRO(KC.LGUI(KC.R), KC.MW_WAIT(250), "https://instagram.com", KC.ENTER)
FB = KC.MACRO(KC.LGUI(KC.R), KC.MW_WAIT(250), "https://facebook.com", KC.ENTER)

# 4. Keymap (12 keys total: 9 matrix + 3 side buttons)
keyboard.keymap = [
    # CHANNEL 1: Media
    [
        KC.MUTE, KC.VOLU, KC.MPLY, 
        KC.VOLD, KC.MNXT, KC.MPRV,
        KC.NO,   KC.NO,   KC.NO,
        KC.TO(0), KC.TO(1), KC.TO(2) 
    ],
    # CHANNEL 2: Socials
    [
        YT,      IG,      FB,
        KC.MW_UP, KC.NO,   KC.NO,
        KC.MW_DN, KC.NO,   KC.NO,
        KC.TO(0), KC.TO(1), KC.TO(2)
    ],
    # CHANNEL 3: Letters
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I,
        KC.TO(0), KC.TO(1), KC.TO(2)
    ]
]

if __name__ == '__main__':
    keyboard.go()