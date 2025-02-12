from machine import Pin
from machine import reset
import time
from motor import *
from PID_control import *
from path import *

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
pid = PIDController(Kp=5.0, Ki=0.0, Kd=0.0)

while True:
  pid.detect_sensor()
  print(pid.sensor_values)
  time.sleep(0.2)
