from machine import Pin
import time
from PID_control import *

# Main control loop
base_speed = 70

def line_detection(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right):
    sensor_value = [p_ll.value(), p_l.value(), p_r.value(), p_rr.value()]
    pid.sensor_values = sensor_value

    error = pid.error_calc()

    dt = 0.001
    correction = pid.correction_calc(error, dt)
    #Time keeping to calculate dt and correction

    # Adjust motor speeds
    left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = left_dir)
    motor_right.speed_change(speed = right_speed, direction = right_dir)

    time.sleep(0.001)