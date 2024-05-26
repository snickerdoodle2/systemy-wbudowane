import pins
import digitalio

BUTTONS = []

for (name, pin) in pins.SWITCHES:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN
    BUTTONS.append((button, name))


while True:
    for (button, name) in BUTTONS:
        if button.value:
            print(name)
