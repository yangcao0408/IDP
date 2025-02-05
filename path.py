from pathblocks import *

# Leaves centre box
def leave_centre(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Leave centre box first
    followline_until(pid, "tjunction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Goes to right collection area
    followline_until(pid, "tjunction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "tjunction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put collection code here



# Path 1 Bottom Right
def path1(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path1_return(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put collection code here

    

# Path 2 Bottom Left
def path2(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path2_return(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Returning Path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)

    # Put collection code here


# Path 3 Top Right
def path3(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)\
    # Put deposit code here, vehicle is facing wall

def path3_return(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put collection code here


# Path 4 Top Left
def path4(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Assuming from right collection area
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put deposit code here, vehicle is facing wall

def path4_return(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Returning path
    # Vehicle is parallel to the destination, facing outwards
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "turn_right", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "right_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Put collection code here


# Returning to starting point when insufficient time
def back(pid, p_ll, p_l, p_r, p_rr, motor_left, motor_right, base_speed = 70):
    # Assuming at collection area, facing collecting area
    # Reverse vehicle direction
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "left_junction", "turn_left", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    followline_until(pid, "t_junction", "forward", p_ll, p_l, p_r, p_rr, motor_left, motor_right, 70)
    # Stop vehicle
