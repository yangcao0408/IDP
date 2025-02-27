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
    dt = 0.001
    correction = pid.correction_calc(error, dt)

    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)
    time.sleep(0.001)

  #After the trigger is detected, whichever action was chosen is then executed
  if action == "turn_left":
    pid.turn_pure_bend(self, left)
    #NOTE: For now this tests all junctions as using the same bending criteria, this may be correct and if so then great but if not then if action == "turn_left" and trigger == "T_Junction" type code must be implemented
  elif action == "turn_right":
    pid.turn_pure_bend(self, right)
  elif action == "forward":
    #This action effectively acts as 'ignore', i.e. upon seeing a junction this action will continue driving straight forwards
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.5)

  #Reinitialise values
  motor_left.speed_change(speed = 90, direction = 0)
  motor_right.speed_change(speed = 90, direction = 0)
  pid.sensor_values = [0, 0, 0, 0]
