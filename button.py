import RPi.GPIO as GPIO
import time
import os
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             GPIO.output(24, True)
             os.system('sudo docker start cam')
             time.sleep(7200)
         else:
             GPIO.output(24, False)
except:
    GPIO.cleanup()
    
    sys.exit()