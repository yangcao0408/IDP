from machine import Pin, PWM
import time

class piston:
    def __init__(self):
        self.piston_speed = PWM(Pin(1))
        self.piston_dir = Pin(0, Pin.OUT)
        self.piston_speed.freq(1000)  # Set PWM frequency to 1kHz
        self.piston_speed.duty_u16(0)  # Set PWM duty cycle to 0 to start the motor as off

    def rise(self):
        self.piston_dir.value(0)
        self.piston_speed.duty_u16(int(65535*100/100))

        #Can still change
        time.sleep(3)
        self.piston_speed.duty_u16(int(65535*0/100))

    def fall(self):
        self.piston_dir.value(1)
        self.piston_speed.duty_u16(int(65535*100/100))

        #Can still change
        time.sleep(3.5)
        self.piston_speed.duty_u16(int(65535*0/100))
