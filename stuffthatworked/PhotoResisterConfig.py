import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

resistorPin = 27
def sensor():
    while True:
        GPIO.setup(resistorPin, GPIO.OUT)
        GPIO.output(resistorPin, GPIO.LOW)
        time.sleep(0.1)
        
        GPIO.setup(resistorPin, GPIO.IN)
        currentTime = time.time()
        diff = 0
        
        while(GPIO.input(resistorPin) == GPIO.LOW):
            diff  = time.time() - currentTime
            
        lightsensor = diff * 1000
        print(lightsensor)
        time.sleep(1)
        while lightsensor > 2:
            return False
        else:
            return True
        
        



            

                



#def is_wet():
 #   GPIO.setmode(GPIO.BCM)
  #  while True:
   #     if(GPIO.input(5)) == 0:
    #        print("Wet")
     #       return True
      #  elif(GPIO.input(5)) == 1:
       #     print("Dry")
        #    return False
        
    #time.sleep(0.25)
