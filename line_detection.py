from machine import Pin
import time
import threading
from motor import *

p_ll = Pin(1, Pin.In) # Input pin for left most sensor
p_l = Pin(2, Pin.In) # Input pin for left sensor
p_r = Pin(3, Pin.In) # Input pin for right sensor
p_rr = Pin(4, Pin.In) # Input pin for right most sensor

light = Pin(5, Pin.Out) # Output pin for light

def blinking(flag):
    if flag == True:
        light.value(not light.value())
        sleep(0.5)




motor_left = Motor_left()
motor_right = Motor_right()


start_time = time.time()

#Put a timer of 4.5 mins
while (time.time() - start_time < 270): # 4.5 mins


    # Lighting
    threading.Timer(0, blinking(flag)).start() # need to set flag when vehicle leaves box
    # Main loop here, with control theory






# If 270 seconds reached
# Write code to return vehicle back to initial position