from machine import Pin, I2C
from machine import reset
import time
from motor import *
from PID_control import *
from path import *
import uasyncio as asyncio

button = Pin(27, Pin.IN, Pin.PULL_DOWN) # Input pin for button
led = Pin(14, Pin.OUT)

sda = Pin(16)
scl = Pin(17) #Set pins
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

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

block_counter = 0

leave_centre_to_collection_base(pid, motor_left, motor_right, led)

#Put a timer of 4.5 mins
while time.ticks_ms() - start_time < 270000 and block_counter < 4:
    pid.reverse(1.5)
    destination = asyncio.run(pickup_destination(pid, motor_left, motor_right, 50, i2c))
    pid.turn_180()
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.4)
    
    if destination == 'B':
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        path1(pid, motor_left, motor_right)
        dropoff(motor_left, motor_right)
        pid.reverse(0.9)
        pid.turn_180()
        path1_return(pid, motor_left, motor_right)
        block_counter += 1

    elif destination == 'A':
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.2)
        path2(pid, motor_left, motor_right)
        dropoff(motor_left, motor_right)
        pid.reverse(0.9)
        pid.turn_180()
        path2_return(pid, motor_left, motor_right)
        block_counter += 1

    elif destination == 'D':
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.2)
        path3(pid, motor_left, motor_right)
        dropoff(motor_left, motor_right)
        pid.reverse(0.9)
        pid.turn_180()
        path3_return(pid, motor_left, motor_right)
        block_counter += 1

    elif destination == 'C':
        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
        time.sleep(0.2)
        path4(pid, motor_left, motor_right)
        dropoff(motor_left, motor_right)
        pid.reverse(0.9)
        pid.turn_180()
        path4_return(pid, motor_left, motor_right)
        block_counter += 1

collection_base_to_centre(pid, motor_left, motor_right, led)

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




