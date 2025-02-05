from machine import Pin, PWM
from time import *

piston_speed = Pin(0, Pin.OUT)
piston_dir = Pin(1, Pin.OUT)

def rise(piston_speed, piston_dir):
    piston_dir.value(0)
    piston_speed.value(100)

    #Can still change
    time.sleep(3)
    piston_speed.value(0)

def fall(piston_speed, piston_dir):
    piston_dir.value(1)
    piston_speed.value(100)

    #Can still change
    time.sleep(4)
    piston_speed.value(0)

