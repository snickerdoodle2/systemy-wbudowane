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
    (1, ARROW_LEFT),
    (2, ARROW_DOWN),
    (3, ARROW_UP),
    (4, ARROW_RIGHT),

    (5, TRIGGER_LEFT),
    (6, BUMPER_LEFT),

    (7, SELECT),
    (8, START),

    (9, TRIGGER_RIGHT),
    (10, BUMPER_RIGHT),

    (11, ACTION_LEFT),
    (12, ACTION_DOWN),
    (13, ACTION_UP),
    (14, ACTION_RIGHT),
]
