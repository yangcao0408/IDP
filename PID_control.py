import time
from motor import *

class PIDController:

    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp #Insert values here
        self.Ki = Ki
        self.Kd = Kd
        self.previous_error = 0
        self.integral = 0
        self.sensor_values = [0, 0, 0, 0] #Place sensor values here

    def error_calc(self):
        #This function takes in a list of binary sensor values and outputs the error value of the system
        weights = [-5, -1, 1, 5]
        #This assigns the weight of each sensor, ideal is therefore zero, while negative requires left turn, positive requires right
        weighted_sum = sum(weight * value for weight, value in zip(weights, self.sensor_values))
        #Negative error implies turn left
        return weighted_sum

    def correction_calc(self, error, dt):
        #This function takes in the error calculated from error_calc and will calculate the required correction based on PID control
        #dt should be set to the time between instances that this function is called

        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        self.previous_error = error
        #Negative correction implies turn left
        return (self.Kp * error + self.Ki * self.integral + self.Kd * derivative)

    def motor_speed(self, base_speed, correction):
        #This function takes a base_speed and the correction from correct_calc to determine the desired motor speed
        left_speed = base_speed + correction
        right_speed = base_speed - correction
        
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

