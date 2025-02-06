import time
from motor import *

class Proportional_Controller:

    def __init__(self, Kp):
        self.Kp = Kp #Insert values here
        self.sensor_values = [0, 0, 0, 0] #Place sensor values here

    def correction_calc(self):
        #This function takes in a list of binary sensor values and outputs the error value of the system
        weights = [-3, -1, 1, 3]
        #This assigns the weight of each sensor, ideal is therefore zero, while negative requires left turn, positive requires right
        weighted_sum = sum(weight * value for weight, value in zip(weights, self.sensor_values))
        #Negative error implies turn left
        return self.Kp * weighted_sum

    def motor_speed(self, base_speed, correction):
        if correction < 0:
          left_speed = base_speed + correction
          right_speed = base_speed
        elif correction > 0:
          left_speed = base_speed
          right_speed = base_speed + correction
        elif correction == 0:
          left_speed = base_speed
          right_speed = base_speed
        
        return left_speed, right_speed

    def turn_left_90(self):
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 70, direction = 0)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(2.2)
        #calibrate how long this turns for

    def turn_right_90(self):
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 70, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(2.2)
        #calibrate how long this turns for

    def detect_sensor(self):
        p_ll = Pin(8, Pin.IN) # Input pin for left most sensor
        p_l = Pin(9, Pin.IN) # Input pin for left sensor
        p_r = Pin(10, Pin.IN) # Input pin for right sensor
        p_rr = Pin(11, Pin.IN) # Input pin for right most sensor

        self.sensor_values = [p_ll.value(), p_l.value(), p_r.value(), p_rr.value()]

    def turn_180(self):
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 70, direction = 0)
        motor_right.speed_change(speed = 70, direction = 1)
