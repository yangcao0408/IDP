# Leaves centre box
def leave(pid, start_flag, entrance_flag, collec_flag):
    # Leave centre box first
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
        start_flag = True # Starts blinking
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass
    
    # Goes to right collection area
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1) and start_flag == True:
        pid.turn_right()
        entrance_flag = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1) and entrance_flag == True:
        pid.turn_right()
        collec_flag = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    # Put collection code here

    return start_flag, entrance_flag, collec_flag



# Path 1 Bottom Right
def path1(pid, collec_flag):
    # Assuming from right collection area
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and collec_flag == True:
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag1 == True:
        pid.turn_left()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    
    # Vehicle is perpendicular to the destination
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag2 == True:
        pid.deposit_box() # Destination reached
        flag1 = 0
        flag2 = 0

    # Returning path


    #Vehicle is parallel to the destination, facing outwards
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
        pid.turn_right()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1) and flag1 == True:
        pid.turn_right()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag2 == True:
        # Go straight to collection
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    # Put collection code here

    

# Path 2 Bottom Left
def path2(pid, collec_flag):
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and collec_flag == True:
        pid.turn_left()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag1 == True:
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    # Vehicle is perpendicular to the destination
    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag2 == True:
        pid.deposit_box()
        flag1 = 0
        flag2 = 0


    # Returning Path
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
        pid.turn_left()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag1 == True:
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag2 == True:
        pid.turn_right()
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    # Put collection code here

# Path 3 Top Right
def path3(pid, collec_flag):
    # Assuming from right collection area
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and collec_flag == True:
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag1 == True:
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag2 == True:
        pid.turn_left()
        flag3 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    # Vehicle is perpendicular to the destination
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag3 == True:
        pid.deposit_box()
        flag1 = 0
        flag2 = 0
        flag3 = 0

    # Returning path
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
        pid.turn_right()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag1 == True:
        pid.turn_right()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag2 == True:
        flag3 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag3 == True:
        # Go straight to collection
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    # Put collection code here

# Path 4 Top Left
def path4(pid, collec_flag):
    # Assuming from right collection area
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and collec_flag == True:
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag1 == True:
        pid.turn_left()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag2 == True:
        flag3 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag3 == True:
        pid.turn_right()
        flag4 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag4 == True:
        pid.deposit_box()
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0

    # Returning path
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
        pid.turn_right()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1) and flag1 == True:
        pid.turn_left()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag2 == True:
        flag3 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag3 == True:
        pid.turn_right()
        flag4 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1) and flag4 == True:
        # Go straight to collection
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass

        # Put collection code here

# Returning to starting point
def back(pid, start_flag):
    # Assuming at collection area, facing collecting area
    if (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
        pid.turn_right()
        flag1 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (0, 1):
            pass
    
    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0) and flag1 == True:
        pid.turn_left()
        flag2 = True
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 0):
            pass

    if (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1) and flag2 == True:
        start_flag = False
        while (pid.sensor_values[0], pid.sensor_values[3]) == (1, 1):
            pass

    return start_flag
