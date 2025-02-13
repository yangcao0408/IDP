from machine import Pin
from main.piston import *

piston1 = piston()

while True:
    piston1.rise()
    print("risen")

    time.sleep(1)
    piston1.fall()
    print("dropped")
