from machine import Pin
import time
import threading
from motor import *
from PID_control import *


motor_left = Motor_left()
motor_right = Motor_right()


start_time = time.time()

# Initialize PID

# Main control loop
base_speed = 20  # Base speed of the robot
motor_left.speed_change(speed = base_speed, direction = 0)
motor_right.speed_change(speed = base_speed, direction = 1)

start_time = time.time()

flag = True # Remove this later

#Put a timer of 4.5 mins
while (time.time() - start_time < 5): # 4.5 mins
    
    # Main loop here, with control theory

    current_time = time.time()
    #Time keeping to calculate dt and correction


# Adjust motor speeds
motor_left.speed_change(speed = 10, direction = 0)
motor_right.speed_change(speed = 10, direction = 0)
#Please note that if motors are placed in a mirrored configuration, their direction of rotation will need to be opposite to drive the same way


# If 270 seconds reached
# Write code to return vehicle back to initial position
