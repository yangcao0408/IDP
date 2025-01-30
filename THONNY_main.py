from machine import Pin
from time import sleep

led = Pin(14, Pin.OUT)
button = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    led.value(button.value())
    sleep(0.1)
    print(button.value())
