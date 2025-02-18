from pathblocks import *
from pickup import *

# Leaves centre box
def leave_centre_to_collection_base(pid, motor_left, motor_right, led):
    # Leave centre box first
    followline_until(pid, "t_junction", "forward", motor_left, motor_right, 90, 0)
    led.value(1)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.7)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.75)
    #This ends at the collection area


# Path 1 Bottom Right (Goes to B)
def path1(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.6)
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.8)
    # Put deposit code here, vehicle is facing wall

def path1_return(pid, motor_left, motor_right):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)
    # Now on the line before collection area i.e. as if reversed
    # Put collection code here

    

# Path 2 Bottom Left (Goes to A)
def path2(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.3)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90, 1.9)
    # Put deposit code here, vehicle is facing wall
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.8)

def path2_return(pid, motor_left, motor_right):
    # Returning Path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 90, 2.0)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)

# Path 3 Top Right (Goes to D)
def path3(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.5)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.5)
    # Put deposit code here, vehicle is facing wall
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.8)

def path3_return(pid, motor_left, motor_right):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.9)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90, 1.9)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)

# Path 4 Top Left (Goes to C)
def path4(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.5)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90, 1.9)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.5)
    # Put deposit code here, vehicle is facing wall
    motor_left.speed_change(speed = 90, direction = 0)
    motor_right.speed_change(speed = 90, direction = 0)
    time.sleep(0.8)

def path4_return(pid, motor_left, motor_right):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.8)
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 90, 2.2)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.8)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90, 0)
    # Put collection code here

# Returning to starting point when insufficient time
def back(pid, motor_left, motor_right, led):
    # Assuming at collection area, facing collecting area
    # Reverse vehicle direction
    pid.reverse(1.0)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90, 2.0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.0)
    followline_until(pid, "t_junction", "forward", motor_left, motor_right, 90, 0)
    led.value(0)
    time.sleep(3)
    motor_left.speed_change(speed = 0, direction = 0)
    motor_right.speed_change(speed = 0, direction = 0)

    # Stop vehicle
