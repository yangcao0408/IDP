import time
from motor import *

class PIDController:

    def __init__(self, Kp):
        self.Kp = Kp #Insert values here
        self.sensor_values = [0, 0, 0, 0] #Place sensor values here

    def error_calc(self):
        #This function takes in a list of binary sensor values and outputs the error value of the system
        weights = [-3, -1, 1, 3]
        #This assigns the weight of each sensor, ideal is therefore zero, while negative requires left turn, positive requires right
        weighted_sum = sum(weight * value for weight, value in zip(weights, self.sensor_values))
        #Negative error implies turn left
        return weighted_sum

    def correction_calc(self, error):
        #Negative correction implies turn left
        return (self.Kp * error)

    def motor_speed(self, base_speed, correction):
        #This function takes a base_speed and the correction from correct_calc to determine the desired motor speed
        left_speed = base_speed + (correction * base_speed / 90)
        right_speed = base_speed - (correction * base_speed / 90) # Making sure that correction at slow speeds are less violent
        
        left_speed_abs = abs(left_speed)
        right_speed_abs = abs(right_speed)

        if left_speed > 0:
            left_dir = 0
        elif left_speed < 0:
            left_dir = 1

        if right_speed > 0:
            right_dir = 0
        elif right_speed < 0:
            right_dir = 1

        return left_speed_abs, right_speed_abs, left_dir, right_dir

    def turn_left_90(self, duration):
        motor_left = Motor_left()
        motor_right = Motor_right()

        motor_left.speed_change(speed = 40, direction = 1)
        motor_right.speed_change(speed = 70, direction = 0)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(duration)
        #calibrate how long this turns for
        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)

    def turn_right_90(self, duration):
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 70, direction = 0)
        motor_right.speed_change(speed = 40, direction = 1)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(duration)
        #calibrate how long this turns for
        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)

    def detect_sensor(self):
        p_ll = Pin(10, Pin.IN) # Input pin for left most sensor
        p_l = Pin(11, Pin.IN) # Input pin for left sensor
        p_r = Pin(12, Pin.IN) # Input pin for right sensor
        p_rr = Pin(13, Pin.IN) # Input pin for right most sensor

        self.sensor_values = [p_ll.value(), p_l.value(), p_r.value(), p_rr.value()]

    def turn_180(self):
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 70, direction = 0)
        motor_right.speed_change(speed = 70, direction = 1)

        time.sleep(2.5)

        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
