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
        weights = [-3, -1, 1, 3]
        #This assigns the weight of each sensor, ideal is therefore zero, while negative requires left turn, positive requires right
        if len(self.sensor_values) != 4:
            return 55
        #55 here behaves as an error code, if we are not reading 4 sensor values
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

    def motor_speed(self, base_speed, correction): #works as forward turn?
        #This function takes a base_speed and the correction from correct_calc to determine the desired motor speed
        left_speed = base_speed + correction
        right_speed = base_speed - correction

        #left_speed and right_speed should never return negative

        left_speed = max(0, min(100, left_speed))  # Assuming motor speed range is 0-100
        right_speed = max(0, min(100, right_speed))

        return left_speed, right_speed

    def turn_left_90():
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 000, direction = 0)
        motor_right.speed_change(speed = 000, direction = 1)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(000)
        #calibrate how long this turns for

    def turn_right_90():
        motor_left = Motor_left()
        motor_right = Motor_right()
                
        motor_left.speed_change(speed = 000, direction = 1)
        motor_right.speed_change(speed = 000, direction = 0)
        #The speed change should be calibrated here for best turning, also the direction will need to be checked based on motor mirroring
        #The ratio of speeds between forwards and backwards must not necessarily be 1:1, do testing

        time.sleep(000)
        #calibrate how long this turns for
