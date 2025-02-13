from machine import Pin, I2C
from machine import reset
import time
from motor import *
from PID_control import *
from path import *

button = Pin(27, Pin.IN, Pin.PULL_DOWN) # Input pin for button
led = Pin(14, Pin.OUT)

'''
sda = Pin(16)
scl = Pin(17) #Set pins
id = 1
i2c = I2C(id=id, sda=sda, scl=scl)
'''

button_flag = 0

def button_pressed(button):
    global button_flag
    if button_flag == 0:
        button_flag = 1

button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

#Button stalling code:
while button_flag == 0:
    time.sleep(0.1)

motor_left = Motor_left()
motor_right = Motor_right()

start_time = time.ticks_ms()

# Initialize PID
pid = PIDController(Kp=15.0)

# Main control loop
base_speed = 90

leave_centre(pid, Motor_left(), Motor_right(), led)

#Put a timer of 4.5 mins
while True:

    destination = go_to_collection(pid, Motor_left(), Motor_right())
    pid.turn_180()
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.5)
    

    if destination == 'A':
        path1(pid, Motor_left(), Motor_right())
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.5)
        dropoff()
        pid.turn_180()
        path1_return(pid, Motor_left(), Motor_right())

    elif destination == 'B':
        path2(pid, Motor_left(), Motor_right())
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.5)
        dropoff()
        pid.turn_180()
        path2_return(pid, Motor_left(), Motor_right())

    elif destination == 'C':
        path3(pid, Motor_left(), Motor_right())
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.5)
        dropoff()
        pid.turn_180()
        path3_return(pid, Motor_left(), Motor_right())

    elif destination == 'D':
        path4(pid, Motor_left(), Motor_right())
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.5)
        dropoff()
        pid.turn_180()
        path4_return(pid, Motor_left(), Motor_right())

'''
leave_centre(pid, Motor_left(), Motor_right(), 1)
go_to_collection(pid, Motor_left(), Motor_right())
motor_left.speed_change(speed = 90, direction = 0)
motor_right.speed_change(speed = 90, direction = 0)
time.sleep(0.5)
pid.turn_180()
path1(pid, Motor_left(), Motor_right())
motor_left.speed_change(speed = 90, direction = 0)
motor_right.speed_change(speed = 90, direction = 0)
time.sleep(0.5)
pid.turn_180()
path1_return(pid, Motor_left(), Motor_right())
followline_until(pid, "left_junction", "turn_left", Motor_left(), Motor_right(), 90)
followline_until(pid, "t_junction", "forward", Motor_left(), Motor_right(), 90)
time.sleep(1.5)
motor_left.speed_change(speed = 0, direction = 0)
motor_right.speed_change(speed = 0, direction = 0)
'''



# If 270 seconds reached
# Write code to return vehicle back to initial position




