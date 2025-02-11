from machine import Pin
from machine import reset
import time
from motor import *
from proportional_control import *
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

control = Proportional_Controller(Kp=6.0)
base_speed = 100
start_time = time.ticks_ms()

#Put a timer of 4.5 mins
while (time.ticks_ms() - start_time < 270000): # 4.5 mins

    control.detect_sensor()
    correction = control.correction_calc()

    # Adjust motor speeds
    left_speed, right_speed = control.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, 0)
    motor_right.speed_change(speed = right_speed, 0)
