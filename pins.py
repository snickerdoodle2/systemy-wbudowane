import board

# GPXX
ANALOG_OUTPUT   = board.GP26
ANALOG_SELECT_A = board.GP5
ANALOG_SELECT_B = board.GP4

ARROW_LEFT  = board.GP2
ARROW_DOWN  = board.GP3
ARROW_UP    = board.GP6
ARROW_RIGHT = board.GP7

TRIGGER_LEFT = board.GP8
BUMPER_LEFT  = board.GP9

SELECT = board.GP10
START = board.GP11

TRIGGER_RIGHT = board.GP12
BUMPER_RIGHT  = board.GP13

ACTION_LEFT = board.GP18
ACTION_DOWN = board.GP19
ACTION_UP = board.GP20
ACTION_RIGHT = board.GP21

SWITCHES = [
    ("ARROW_LEFT", ARROW_LEFT),
    ("ARROW_DOWN", ARROW_DOWN),
    ("ARROW_UP", ARROW_UP),
    ("ARROW_RIGHT", ARROW_RIGHT),

    ("TRIGGER_LEFT", TRIGGER_LEFT),
    ("BUMPER_LEFT", BUMPER_LEFT),

    ("SELECT", SELECT),
    ("START", START),

    ("TRIGGER_RIGHT", TRIGGER_RIGHT),
    ("BUMPER_RIGHT", BUMPER_RIGHT),

    ("ACTION_LEFT", ACTION_LEFT),
    ("ACTION_DOWN", ACTION_DOWN),
    ("ACTION_UP", ACTION_UP),
    ("ACTION_RIGHT", ACTION_RIGHT),
]