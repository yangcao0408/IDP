from machine import Pin
from machine import reset
import time
from motor import *
from PID_control import *

def followline_until(trigger, action):
  if trigger == left_junct:
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[1] * (1 - pid.sensor_values[3])
  elif trigger == right_junct:
    trigger_value = lambda: (1 - pid.sensor_values[0]) * pid.sensor_values[2] * pid.sensor_values[3])
  elif trigger == t_junct:
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[3]
  #trigger_value has value 1 when it is activated

  while trigger_value != 1:
    sensor_value = [p_ll.value(), p_l.value(), p_r.value(), p_rr.value()]
    pid.sensor_values = sensor_value

    error = pid.error_calc()

    current_time = time.ticks_ms()
    dt = current_time - last_time
    last_time = current_time
    correction = pid.correction_calc(error, dt)

    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)
    time.sleep(0.001)

  if action == turn_left:
    pid.turn_left_90()
  elif action == turn_right:
    pid.turn_right_90()
  elif action == forward:
    motor_left.speed_change(speed = 70, direction = 0)
    motor_right.speed_change(speed = 70, direction = 0)
    time.sleep(0.5)
    # Reinitialise
    motor_left.speed_change(speed = 0, direction = 0)
    motor_right.speed_change(speed = 0, direction = 0)
