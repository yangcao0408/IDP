from machine import Pin, PWM

class Motor_left:
 def __init__(self):
    self.m1Dir = Pin(7 , Pin.OUT) # set pin left wheel
    self.pwm1 = PWM(Pin(6))
    self.pwm1.freq(1000)
    self.pwm1.duty_u16(0)
 def off(self):
    self.pwm1.duty_u16(0)
 def speed_change(self, speed, direction):
    self.pwm1.duty_u16(int(65535*speed/100))
    self.m1Dir.value(direction)
    #direction: forward = 0, reverse = 1

class Motor_right:
 def __init__(self):
    self.m2Dir = Pin(4 , Pin.OUT) # set pin left wheel
    self.pwm2 = PWM(Pin(5))
    self.pwm2.freq(1000)
    self.pwm2.duty_u16(0)
 def off(self):
    self.pwm2.duty_u16(0)
 def speed_change(self, speed, direction):
    self.pwm2.duty_u16(int(65535*speed/100))
    self.m2Dir.value(direction)
