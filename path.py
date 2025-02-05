from pathblocks import *

# Leaves centre box
def leave_centre(pid, motor_left, motor_right, light):
    # Leave centre box first
    followline_until(pid, "tjunction", "forward", motor_left, motor_right, 70)
    light.value(1)


    
def go_to_collection(pid, motor_left, motor_right):    
    # Goes to right collection area
    followline_until(pid, "tjunction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "tjunction", "turn_right", motor_left, motor_right, 70)
    # Put collection code here



# Path 1 Bottom Right
def path1(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path1_return(pid, motor_left, motor_right):
    # Returning path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    # Put collection code here

    

# Path 2 Bottom Left
def path2(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path2_return(pid, motor_left, motor_right):
    # Returning Path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)

    # Put collection code here


# Path 3 Top Right
def path3(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)\
    # Put deposit code here, vehicle is facing wall

def path3_return(pid, motor_left, motor_right):
    # Returning path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    # Put collection code here


# Path 4 Top Left
def path4(pid, motor_left, motor_right):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path4_return(pid, motor_left, motor_right):
    # Returning path
    pid.turn_180()
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", motor_left, motor_right, 70)
    # Put collection code here


# Returning to starting point when insufficient time
def back(pid, motor_left, motor_right):
    # Assuming at collection area, facing collecting area
    # Reverse vehicle direction
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", motor_left, motor_right, 70)

def back_centre(pid, motor_left, motor_right, light):
    # Assuming vehicle facing blocks
    pid.turn_180()
    followline_until(pid, "t_junction", "forward", motor_left, motor_right, 70)
    light.value(0)
    # Stop vehicle
