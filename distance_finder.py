# import time
from machine import Pin, I2C
from vl53l0x import VL53L0X

def return_range_mm(i2c):
  tof = VL53L0X(i2c)
  budget = tof.measurement_timing_budget_us
  tof.set_measurement_timing_budget(40000)

  # tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
  tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)

  # tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
  tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)
  
  return tof.ping()-50
