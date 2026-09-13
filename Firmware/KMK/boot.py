import board
import digitalio
import storage

# Bypass pin (Channel Button 1)
# Wiring: GP6 -> Button -> 3.3V
button = digitalio.DigitalInOut(board.GP6)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN 

# If the button is NOT pressed, hide the drive from the PC
if not button.value:
    storage.disable_usb_drive()