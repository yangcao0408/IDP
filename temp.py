from machine import Pin
from machine import reset
import time
from motor import *
from PID_control import *
from path import *

light = Pin(12, Pin.OUT) # Output pin for light

button = Pin(28, Pin.IN, Pin.PULL_DOWN) # Input pin for button

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
pid = PIDController(Kp=4.0, Ki=0.01, Kd=0.0)

# Main control loop
base_speed = 70
last_time = time.ticks_ms()
time.sleep(0.001)



#Put a timer of 4.5 mins
while (time.ticks_ms() - start_time < 270000): # 4.5 mins
    motor_left.speed_change(speed = 70, direction = 0)
    motor_right.speed_change(speed = 70, direction = 0)


# If 270 seconds reached
# Write code to return vehicle back to initial position



