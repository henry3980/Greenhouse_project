import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)

def is_wet():
    GPIO.setmode(GPIO.BCM)
    while True:
        if(GPIO.input(5)) == 0:
            print("Wet")
            return True
        elif(GPIO.input(5)) == 1:
            print("Dry")
            return False
        
    time.sleep(0.25)



