# import time
from machine import Pin, I2C
from vl53l0x import VL53L0X

def return_range_mm(tof):
  #Returns distance in mm, without correction
  return tof.ping()
