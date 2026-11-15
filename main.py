# Test!!!
from screen import Display

from grove.grove_button import GroveButton
import RPi.GPIO as GPIO
from time import sleep

# GPIOs pour tout
BOUTON          = 5
BUZZER          = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

ecran           = Display()
bouton          = GroveButton(BOUTON)
def on_press(t):
    GPIO.output(BUZZER, 1)
    for y in range(128):
        ligne = ecran.modifie_ligne(y)
        for x in range(128):
            ligne[x] = 1
    ecran.push()
def on_release(t):
    GPIO.output(BUZZER, 0)
    for y in range(128):
        ligne = ecran.modifie_ligne(y)
        for x in range(128):
            ligne[x] = 0
    ecran.push()
bouton.on_press = on_press
bouton.on_release = on_release

while True:
    sleep(1)
