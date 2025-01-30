from machine import Pin
import time
from motor import *
from PID_control import *

p_ll = Pin(8, Pin.IN) # Input pin for left most sensor
p_l = Pin(9, Pin.IN) # Input pin for left sensor
p_r = Pin(10, Pin.IN) # Input pin for right sensor
p_rr = Pin(11, Pin.IN) # Input pin for right most sensor

light = Pin(5, Pin.OUT) # Output pin for light

#button = Pin(6, Pin.IN, Pin.PULL_DOWN) # Input pin for button

#def blinking(flag):
    #if flag == True: # If vehicle leaves the box
        #light.value(not light.value())
        #time.sleep(0.5)

motor_left = Motor_left()
motor_right = Motor_right()


start_time = time.time()

# Initialize PID
pid = PIDController(Kp=1.0, Ki=0.1, Kd=0.05)

# Main control loop
base_speed = 30  # Base speed of the robot
last_time = time.time()

#flag = True # Remove this later

#Put a timer of 4.5 mins
while (time.time() - start_time < 270): # 4.5 mins
    
    # Lighting
    #threading.Timer(0, blinking(flag)).start() # need to set flag when vehicle leaves box
    # Main loop here, with control theory
    sensor_value = [p_ll.value(), p_l.value(), p_r.value(), p_rr.value()]
    pid.sensor_values = sensor_value

    error = pid.error_calc()

    current_time = time.time()
    dt = current_time - last_time
    correction = pid.correction_calc(error, dt)
    last_time = current_time
    #Time keeping to calculate dt and correction

    # Adjust motor speeds
    left_speed, right_speed = pid.motor_speed(base_speed, correction)
    motor_left.speed_change(speed = left_speed, direction = 0)
    motor_right.speed_change(speed = right_speed, direction = 0)
    #Please note that if motors are placed in a mirrored configuration, their direction of rotation will need to be opposite to drive the same way


# If 270 seconds reached
# Write code to return vehicle back to initial position
