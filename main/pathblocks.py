from machine import Pin
from machine import reset
import time
from motor import *
from PID_control import *

def followline_until(pid, trigger, action, motor_left, motor_right, base_speed, duration):
  if trigger == "left_junction":
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[1] * (1 - pid.sensor_values[3])
  elif trigger == "right_junction":
    trigger_value = lambda: ((1 - pid.sensor_values[0]) * pid.sensor_values[2] * pid.sensor_values[3])
  elif trigger == "t_junction":
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[3]
  #trigger_value has value 1 when it is activated
  
  iter = 0
  while trigger_value() != 1:
    pid.detect_sensor()

    if iter == 200:
      print(left_speed, right_speed)
      iter = 0
    iter += 1

    error = pid.error_calc()
    dt = 0.001
    correction = pid.correction_calc(error, dt)

    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)
    time.sleep(0.001)

  if action == "turn_left":
    pid.turn_left_90(duration)
  elif action == "turn_right":
    pid.turn_right_90(duration)
  elif action == "forward":
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.5)
  elif action == "stop":
    motor_left.speed_change(speed = 0, direction = 0)
    motor_right.speed_change(speed = 0, direction = 0)
    time.sleep(4.0)
  elif action == "reverse":
    motor_left.speed_change(speed = 70, direction = 1)
    motor_right.speed_change(speed = 70, direction = 1)
    time.sleep(0.3)
  # Reinitialise
  motor_left.speed_change(speed = 90, direction = 0)
  motor_right.speed_change(speed = 90, direction = 0)
  pid.sensor_values = [0, 0, 0, 0]
