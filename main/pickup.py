import machine
import time
from piston import *
from QR import *
from distance_finder import *
from piston import *

def pickup_destination(pid, motor_left, motor_right, base_speed = 50):
    flag_trigger = False
    scan_trigger = False

    motor_left.speed_change(speed = 50, direction = 0)
    motor_right.speed_change(speed = 50, direction = 0)
    
    while flag_trigger == False:
        print("flag_trigger: ", flag_trigger)
        print("scan trigger: ", scan_trigger)

        pid.detect_sensor()

        error = pid.error_calc()
        correction = pid.correction_calc(error)

        left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
        motor_left.speed_change(speed = left_speed, direction = left_dir)
        motor_right.speed_change(speed = right_speed, direction = right_dir)

        #Put QR code scanning here
        QR_code = QR.scan_for_QR()
        if QR_code!= 0 and scan_trigger == False:
            scan_trigger = True
            destination = QR

            dummy_start = time.time()

        if scan_trigger == True:
            #Dummy code whilst ToF is broken
            if time.time() - dummy_start > 2:
                flag_trigger = True
            
            #distance = return_range_mm() #adjust distance_finder file
            #Distance to be determined
            #if distance < 5:
                #flag_trigger = True
                
    # Assuming forklift is below block
    pist = piston()
    pist.rise()
    return(destination)

def dropoff():
    pist = piston()
    pist.fall()
    
