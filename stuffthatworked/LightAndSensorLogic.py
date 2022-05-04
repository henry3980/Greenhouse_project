#
from PhotoResisterConfig import *
from led import *

def check_if_light_needed():
    
    islight = sensor()
    if islight == True:
        print("It's light enough")
        lightsoff()
    else:
        print("~~~~LED is turned on~~~~")
        lightson()
            

    
