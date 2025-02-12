from machine import Pin
import time

p_ll = Pin(12, Pin.IN)

while True:
    print(p_ll.value())
    time.sleep(0.2)

