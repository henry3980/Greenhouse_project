
#imports functions from our logic files
from LightAndSensorlogic import *
from moistureAndPumplogic import *


while True:
    # gets water and light logic files to check water/light levels and enable functions if required
    Check_If_Water_Needed()
    check_if_light_needed()
