#stolen from the internet this file controls the led when called upon by the Light
# and sensor logic file

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#imports required modules
import time
import board
import neopixel


pixel_pin = board.D21


# The number of NeoPixels in our strip(inflated by 4 due to technical errors)
num_pixels = 12


#telling the pi which way our lights are wired
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!

ORDER = neopixel.GRB

#defining a pixel for the neopixel modules
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


#function that sets pixel brightness to 0(off)
def lightsoff():
    pixels.fill((0, 0, 0))
    pixels.show()

#function that turns the neo pixel to brightest(on)
def lightson():

    pixels.fill((255, 255, 255))
    
    pixels.show()
    
   
