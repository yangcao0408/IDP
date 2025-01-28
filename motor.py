from machine import Pin, PWM

class Motor_left:
 def __init__(self):
    self.m1Dir = Pin(6 , Pin.OUT) # set pin left wheel
    self.pwm1 = PWM(Pin(7))
    self.pwm1.freq(1000)
    self.pwm1.duty_u16(0)
 def off(self):
    self.pwm1.duty_u16(0)
 def Forward(self):
    self.m1Dir.value(0) # forward = 0 reverse = 1 motor 1
    self.pwm1.duty_u16(int(65535*100/100)) # speed range 0-100 motor 2
 def Reverse(self):
    self.m1Dir.value(1)
    self.pwm1.duty_u16(int(65535*30/100))
 def speed_change(self, speed):
    self.pwm1.duty_u16(int(65535*speed/100))
 def direction_change(self, direction): # 0 = forward, 1 = reverse
    self.m2Dir.value(direction)

class Motor_right:
 def __init__(self):
    self.m2Dir = Pin(10 , Pin.OUT) # set pin left wheel
    self.pwm2 = PWM(Pin(9))
    self.pwm2.freq(1000)
    self.pwm2.duty_u16(0)
 def off(self):
    self.pwm2.duty_u16(0)
 def Forward(self):
    self.m2Dir.value(0) # forward = 0 reverse = 1 motor 2
    self.pwm2.duty_u16(int(65535*100/100)) # speed range 0-100 motor 2
 def Reverse(self):
    self.m2Dir.value(1)
    self.pwm2.duty_u16(int(65535*30/100))
 def speed_change(self, speed):
    self.pwm1.duty_u16(int(65535*speed/100))
 def direction_change(self, direction): # 0 = forward, 1 = reverse
    self.m2Dir.value(direction)