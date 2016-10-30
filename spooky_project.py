# Combine with a PIR (Passive Infared) sensor on GPIO 17 and some
# spooky sounds for fun Halloween times!

# the sounds need to be .wav files and named "1.wav" through "6.wav" 
# and placed in "/home/pi/Music/scary/"
# They must also be compatible with aplay.

import RPi.GPIO as GPIO
import os
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):

    if GPIO.input(17)==1:

        sfx = randint(1,6)
        os.system("aplay /home/pi/Music/scary/" + str(sfx) + ".wav")
        sleep(300)

GPIO.cleanup()
