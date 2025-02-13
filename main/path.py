from pathblocks import *
from pickup import *

# Leaves centre box
def leave_centre_to_collection_base(pid, motor_left, motor_right, led):
    # Leave centre box first
    followline_until(pid, "t_junction", "forward", motor_left, motor_right, 90, 0)
    led.value(1)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    #This ends at the collection area

def collection_base_to_centre(pid, motor_left, motor_right, led):
    #insert stuff here
    led.value(0)


# Path 1 Bottom Right
def path1(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90, 0)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 1.9)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90, 2.0)
    # Put deposit code here, vehicle is facing wall

def path1_return(pid, motor_left, motor_right):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90, 1.6)
    #########Changed for testing purposes
    #########
    #########
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90, 1.8)
    # Put collection code here

    

# Path 2 Bottom Left
def path2(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90)
    # Put deposit code here, vehicle is facing wall

def path2_return(pid, motor_left, motor_right):
    # Returning Path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90)

    # Put collection code here


# Path 3 Top Right
def path3(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)\
    # Put deposit code here, vehicle is facing wall

def path3_return(pid, motor_left, motor_right):
    # Returning path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90)
    # Put collection code here


# Path 4 Top Left
def path4(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)
    # Put deposit code here, vehicle is facing wall

def path4_return(pid, motor_left, motor_right):
    # Returning path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90)
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 90)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 90)
    # Put collection code here


# Returning to starting point when insufficient time
def back(pid, motor_left, motor_right):
    # Assuming at collection area, facing collecting area
    # Reverse vehicle direction
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 90)

def back_centre(pid, motor_left, motor_right, light):
    # Assuming vehicle facing blocks
    pid.turn_180()
    followline_until(pid, "t_junction", "forward", motor_left, motor_right, 90)
    light.value(0)
    # Stop vehicle
