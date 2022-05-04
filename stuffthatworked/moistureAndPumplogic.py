from moisture_sensor import is_wet
from sol_code import pump
from sol_code import notpump


def Check_If_Water_Needed():
    

    wet = is_wet()

    if wet == False:
        pump()
       
    else:
        notpump()

pumping()