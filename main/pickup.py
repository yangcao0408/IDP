import machine
import time
from piston import *
from QR import *
from distance_finder import *

def pickup(pid, motor_left, motor_right, base_speed):
    flag_trigger = lambda: False
    scan_trigger = lambda: False
    
    while flag_trigger != True:
        pid.detect_sensor()

        error = pid.error_calc()
        correction = pid.correction_calc(error)

        left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
        motor_left.speed_change(speed = left_speed - 20, direction = left_dir)
        motor_right.speed_change(speed = right_speed - 20, direction = right_dir)

        #Put QR code scanning here
        QR = QR.scan_for_QR()
        if QR != 0 and scan_trigger == False:
            scan_trigger = True

        if scan_trigger == True:
            distance = return_range_mm() #adjust distance_finder file
            #Distance to be determined
            if distance < 5:
                flag_trigger = True
                
    # Assuming forklift is below block
    rise()

def dropoff():
    fall()
    
