# import time
from machine import Pin, I2C
from vl53l0x import VL53L0X
import time
from main.piston import *
from main.distance_finder import *

tof_sda = Pin(18)
tof_scl = Pin(19)
tof_id = 1
tof_i2c = I2C(id=tof_id, sda=tof_sda, scl=tof_scl)
tof = VL53L0X(tof_i2c)
tof.set_measurement_timing_budget(40000)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

while True:
    print(return_range_mm(tof))