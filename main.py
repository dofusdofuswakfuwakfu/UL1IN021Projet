# Test!!!
from screen import Display

from grove.grove_button import GroveButton
from grove.grove_thumb_joystick import GroveThumbJoystick as GroveJoystick
import RPi.GPIO as GPIO
from time import sleep

# GPIOs pour tout
BOUTON          = 5
BUZZER          = 12
JOYSTICK        = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

ecran           = Display()
bouton          = GroveButton(BOUTON)
joystick        = GroveJoystick(JOYSTICK)

last_read       = (500, 500)

def to_screen(read):
    return ((127*read[0])//1000), ((127*read[1])//1000)

def on_press(t):
    pass
def on_release(t):
    pass
bouton.on_press = on_press
bouton.on_release = on_release

while True:
    last_read = joystick.value
    sp = to_screen(last_read) # sapphire panlogism
    ligne = ecran.modifie_ligne(sp[1])
    ligne[sp[0]] = 1
    ecran.push()
    sleep(1/30)
