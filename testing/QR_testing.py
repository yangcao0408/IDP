from machine import Pin, I2C
from QR import *

QR_scl = Pin(17, Pin.IN)
QR_sda = Pin(16, Pin.IN)

i2c = I2C(1, scl=QR_scl, sda=QR_sda, freq=400000)


while True:
    print(scan_for_QR(0.2, i2c))
    time.sleep(0.2)