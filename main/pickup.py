from machine import Pin, I2C
import time
from piston import *
from QR import *
from distance_finder import *
from piston import *
import uasyncio as asyncio
from vl53l0x import VL53L0X

async def scan_QR_concurrently(i2c, scan_trigger, destination):
    #Asynchronously scans for a QR code and sets scan_trigger when detected.
    while True:
        QR_code = scan_for_QR(0.1, i2c)
        if QR_code != 0:
            scan_trigger.set()  # Notify that QR has been found
            destination.append(QR_code)  # Store destination
            print('destination:', QR_code)
            break  # Stop scanning once QR is found
        await asyncio.sleep(0.1)  # Yield execution

async def check_tof_sensor(tof_trigger):
    #Asynchronously monitors the ToF sensor after QR scan.
    print("Starting ToF sensor monitoring...")

    tof_sda = Pin(18)
    tof_scl = Pin(19)
    tof_id = 1
    tof_i2c = I2C(id=tof_id, sda=tof_sda, scl=tof_scl)
    tof = VL53L0X(tof_i2c)
    tof.set_measurement_timing_budget(40000)
    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

    distance = 999  # Dummy initial value
    while distance >= 100:  # Keep checking distance until below 100mm
        distance = return_range_mm(tof)
        #print('Distance:', distance)
        if distance < 100:
            tof_trigger.set()  # Notify that ToF condition is met
            time.sleep(0.1) # Wait for block to get slotted in
            break
        await asyncio.sleep(0.1)  # Yield execution

async def line_following(pid, motor_left, motor_right, base_speed, stop_event):
    #Continuously runs line following until stop_event is set.
    while not stop_event.is_set():
        pid.detect_sensor()
        error = pid.error_calc()
        correction = pid.correction_calc(error)

        left_speed, right_speed, left_dir, right_dir = pid.motor_speed(base_speed, correction)
        motor_left.speed_change(speed=left_speed, direction=left_dir)
        motor_right.speed_change(speed=right_speed, direction=right_dir)

        await asyncio.sleep(0.01)  # Yield execution to other tasks

async def pickup_destination(pid, motor_left, motor_right, base_speed, i2c):
    #Runs line following, QR scanning, and ToF sensor checking asynchronously.
    scan_trigger = asyncio.Event()  # QR code detection flag
    tof_trigger = asyncio.Event()   # ToF sensor flag
    destination = []  # Store destination

    # Start line following
    stop_event = asyncio.Event()
    line_follow_task = asyncio.create_task(line_following(pid, motor_left, motor_right, base_speed, stop_event))

    # Run QR scanning and ToF sensor check **concurrently**
    qr_task = asyncio.create_task(scan_QR_concurrently(i2c, scan_trigger, destination))
    tof_task = asyncio.create_task(check_tof_sensor(tof_trigger))

    # Wait for both QR scanning and ToF sensor check to complete
    await asyncio.gather(qr_task, tof_task)

    print("QR scan and ToF sensor check completed. Stopping.")

    # Stop motors **after both tasks are done**
    stop_event.set()
    await line_follow_task  # Ensure line following stops cleanly
    motor_left.speed_change(speed=0, direction=0)
    motor_right.speed_change(speed=0, direction=0)

    # Assuming forklift action below
    pist = piston()
    pist.rise()
    
    return destination[0]



def dropoff(motor_left, motor_right):
    motor_left.speed_change(speed = 0, direction = 0)
    motor_right.speed_change(speed = 0, direction = 0)
    pist = piston()
    pist.fall()
    
