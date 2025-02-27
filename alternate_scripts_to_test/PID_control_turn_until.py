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
        weights = [-2, -1, 1, 2]
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

    def turn_pure_bend(self, LorR):
        motor_left = Motor_left()
        motor_right = Motor_right()

        if LoR == right:
            LoRvalue = 3
        elif LoR == left:
            LoRvalue = 0

        motor_left.speed_change(speed = 50, direction = 1)
        motor_right.speed_change(speed = 70, direction = 0)

        time.sleep(0.2)
        #Sleep to allow for some movement before to avoid sensor tripping from initial state
        
        #This assumes that e.g. for a left turn, LL will be off until the final position where it flicks on
        #PLEASE NOTE: All turning methods use the same sensor parameters, this is the simplest way and may or may not work, adjust while testing
        while self.sensor_values[LoRvalue] != 1
            time.sleep(0.0001)

        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)

    def turn_tjunction(self, LorR):
        motor_left = Motor_left()
        motor_right = Motor_right()

        if LoR == right:
            LoRvalue = 3
        elif LoR == left:
            LoRvalue = 0

        motor_left.speed_change(speed = 50, direction = 1)
        motor_right.speed_change(speed = 70, direction = 0)

        time.sleep(0.2)
        #Sleep to allow for some movement before to avoid sensor tripping from initial state
        
        #This assumes that e.g. for a left turn, LL will be off until the final position where it flicks on
        #This is the same as purebend
        while self.sensor_values[LoRvalue] != 1
            time.sleep(0.0001)

        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)

    def turn_combijunction(self, LorR):
        motor_left = Motor_left()
        motor_right = Motor_right()

        if LoR == right:
            LoRvalue = 3
        elif LoR == left:
            LoRvalue = 0

        motor_left.speed_change(speed = 50, direction = 1)
        motor_right.speed_change(speed = 70, direction = 0)

        time.sleep(0.2)
        #Sleep to allow for some movement before to avoid sensor tripping from initial state
        
        #This assumes that e.g. for a left turn, LL will be off until the final position where it flicks on
        #This is the same as purebend
        while self.sensor_values[LoRvalue] != 1
            time.sleep(0.0001)

        motor_left.speed_change(speed = 0, direction = 0)
        motor_right.speed_change(speed = 0, direction = 0)

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

        time.sleep(2.9)

        motor_left.speed_change(speed = 90, direction = 0)
        motor_right.speed_change(speed = 90, direction = 0)
