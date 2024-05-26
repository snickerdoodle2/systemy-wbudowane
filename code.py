import pins
import digitalio
import analogio
import adafruit_hid
import usb_hid

from hid_gamepad import Gamepad

BUTTONS = []

gamepad = Gamepad(usb_hid.devices)

print("Ready!")

analog = analogio.AnalogIn(pins.ANALOG_INPUT)

select_a = digitalio.DigitalInOut(pins.ANALOG_SELECT_A)
select_a.direction = digitalio.Direction.OUTPUT

select_b = digitalio.DigitalInOut(pins.ANALOG_SELECT_B)
select_b.direction = digitalio.Direction.OUTPUT

# SETUP SWITCHES
for (id, pin) in pins.SWITCHES:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    BUTTONS.append((button, id))

def get_joystick_value(id):
    select_a.value = id % 2
    select_b.value = (id >> 1) % 2

    return int((analog.value * 256) / 65536 - 128)


while True:
    toPress = []
    toRelease = []
    for (button, id) in BUTTONS:
        if button.value:
            toPress.append(id)
        else:
            toRelease.append(id)

    gamepad.move_joysticks(-get_joystick_value(1), get_joystick_value(0), -get_joystick_value(3), get_joystick_value(2))

    gamepad.press_buttons(*toPress)
    gamepad.release_buttons(*toRelease)
