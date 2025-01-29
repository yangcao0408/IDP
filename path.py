# Leaves centre box
def leave(pid):
    # Leave centre box first
    if pid.sensor_values() == [1, 1, 1, 1]:
        flag = True # Starts blinking
        while pid.sensor_values() == [1, 1, 1, 1]:
            pass
    
    # Goes to right collection area
    if pid.sensor_values() == [1, 1, 1, 1] and flag == True:
        pid.turn_right()
        flag1 = True
        while pid.sensor_values() == [1, 1, 1, 1]:
            pass

    if pid.sensor_values() == [1, 1, 1, 1] and flag1 == True:
        pid.turn_right()
        flag2 = True
        while pid.sensor_values() == [1, 1, 1, 1]:
            pass

    # Put collection code here



# Path 1 Bottom Right
def path1(pid):
    # Assuming from right collection area
    if pid.sensor_values() == [1, 1, 0, 0] and flag1 == True:
        flag2 = True
        while pid.sensor_values() == [1, 1, 0, 0]:
            pass
    
    if pid.sensor_values() == [1, 1, 0, 0] and flag2 == True:
        pid.turn_left()
        flag3 = True
        while pid.sensor_values() == [1, 1, 0, 0]:
            pass

    
    # Vehicle is perpendicular to the destination
    if pid.sensor_values() == [1, 1, 0, 0] and flag3 == True:
        pid.deposit_box() # Destination reached
        flag1 = 0
        flag2 = 0
        flag3 = 0

    # Returning path


    #Vehicle is parallel to the destination, facing outwards
    if pid.sensor_values() == [1, 1, 1, 1]:
        pid.turn_right()
        flag1 = True
        while pid.sensor_values() == [1, 1, 1, 1]:
            pass

    if pid.sensor_values() == [1, 1, 1, 1] and flag1 == True:
        pid.turn_right()
        flag2 = True
        while pid.sensor_values() == [1, 1, 1, 1]:
            pass

    if pid.sensor_values() == [0, 0, 1, 1] and flag2 == True:
        # Go straight to collection
        flag3 = True
        while pid.sensor_values() == [0, 0, 1, 1]:
            pass

    # Put collection code here

    

# Path 2

# Path 3

# Path 4