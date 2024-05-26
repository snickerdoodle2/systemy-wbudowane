import pins
import digitalio
import adafruit_hid
import usb_hid

from hid_gamepad import Gamepad

BUTTONS = []

gamepad = Gamepad(usb_hid.devices)

print("Ready!")

# SETUP SWITCHES
for (id, pin) in pins.SWITCHES:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    BUTTONS.append((button, id))


while True:
    toPress = []
    toRelease = []
    for (button, id) in BUTTONS:
        if button.value:
            toPress.append(id)
        else:
            toRelease.append(id)

    gamepad.press_buttons(*toPress)
    gamepad.release_buttons(*toRelease)
