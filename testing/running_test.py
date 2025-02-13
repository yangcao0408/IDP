from machine import Pin
from main.PID_control import *
from main.motor import *

Motor_left = Motor_left()
Motor_right = Motor_right()

pid = PIDController(Kp=15.0)


while True:
    pid.detect_sensor()

    error = pid.error_calc()
    correction = pid.correction_calc(error)

    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)