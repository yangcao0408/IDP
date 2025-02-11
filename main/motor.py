from machine import Pin, PWM
#This module defines each motor as a class, setting up speed setting as a method and pinouts in the initialisation of each class

class Motor_left:
 def __init__(self):
    self.m1Dir = Pin(7 , Pin.OUT) # set pin left wheel
    self.pwm1 = PWM(Pin(6))
    self.pwm1.freq(1000)
    self.pwm1.duty_u16(0)
    #This block initialises pins for direction and pwm control
    #PWM frequency is set to 1kHz and the PWM duty cycles initialised to 0 to start the motor as off
 def off(self):
    self.pwm1.duty_u16(0)
    #This method sets PWM duty cycle to 0, turning off the motor
 def speed_change(self, speed, direction):
    self.pwm1.duty_u16(int(65535*speed/100))
    self.m1Dir.value(direction)
    #direction: forward = 0, reverse = 1
    #This method scales the PWM duty cycle up to its maximum according to the percentage given in the speed input, and also sets the direction of the motor

#The following class is the same as that above but adjusted for the opposite motor
class Motor_right:
 def __init__(self):
    self.m2Dir = Pin(4 , Pin.OUT) # set pin right wheel
    self.pwm2 = PWM(Pin(5))
    self.pwm2.freq(1000)
    self.pwm2.duty_u16(0)
 def off(self):
    self.pwm2.duty_u16(0)
 def speed_change(self, speed, direction):
    self.pwm2.duty_u16(int(65535*speed/100))
    self.m2Dir.value(direction)
    #direction: forward = 0, reverse = 1
