from machine import Pin
import time

light_sensor = Pin(18, Pin.IN)

print(light_sensor.value())
