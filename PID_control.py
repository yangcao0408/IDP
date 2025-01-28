import time

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

    def motor_speed(base_speed, correction):
        #This function takes a base_speed and the correction from correct_calc to determine the desired motor speed
        left_speed = base_speed + correction
        right_speed = base_speed - correction

        #left_speed and right_speed should never return negative

        left_speed = max(0, min(100, left_speed))  # Assuming motor speed range is 0-100
        right_speed = max(0, min(100, right_speed))

        return left_speed, right_speed

# Initialize PID
pid = PIDController(Kp=1.0, Ki=0.1, Kd=0.05)

# Main control loop
base_speed = 50  # Base speed of the robot
last_time = time.time()

while True:
    sensor_values = [1, 0, 1, 0]  # Replace with actual sensor input

    error = pid.calculate_error(sensor_values)

    current_time = time.time()
    dt = current_time - last_time
    correction = pid.compute(error, dt)
    last_time = current_time
    #Time keeping to calculate dt and correction

    # Adjust motor speeds
    left_speed, right_speed = pid.motor_speed(base_speed, correction)

