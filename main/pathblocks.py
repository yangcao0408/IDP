from machine import Pin
from machine import reset
import time
from motor import *
from PID_control import *

#The goal of pathblocks is to segment and systematise stages of the path into reuseable standard elements
#These elements can then be followed one after another to form a given path

def followline_until(pid, trigger, action, motor_left, motor_right, base_speed, duration):
  #This function takes a trigger and action and will follow the straight line until a given trigger is detected, then will perform the chosen action e.g. follow the line until a left junction then turn left
  
  #This section corresponds chosen triggers to their sensor conditions
  if trigger == "left_junction":
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[1] * (1 - pid.sensor_values[3])
    #trigger_value will return 1 when the trigger has been detected, for example here left_junction trigger is LL * L * NOT(RR), i.e. both left side sensors are on but rightmost is off
    #lambda function has been used here to keep trigger_value as a continually updating dynamic variable rather than a static variable
  elif trigger == "right_junction":
    trigger_value = lambda: ((1 - pid.sensor_values[0]) * pid.sensor_values[2] * pid.sensor_values[3])
  elif trigger == "t_junction":
    trigger_value = lambda: pid.sensor_values[0] * pid.sensor_values[3]

  #The following loops line following until the trigger is detected
  while trigger_value() != 1:
    pid.detect_sensor()

    error = pid.error_calc()
    correction = pid.correction_calc(error)

    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)

  #After the trigger is detected, whichever action was chosen is then executed
  if action == "turn_left":
    pid.turn_left_90(duration)
  elif action == "turn_right":
    pid.turn_right_90(duration)
  elif action == "forward":
    #This action effectively acts as 'ignore', i.e. upon seeing a junction this action will continue driving straight forwards
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
