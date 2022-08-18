import pigpio
from src.servo import Servo

class SG92R(Servo):
    def __init__(self, PwmPinNumber: int) -> None:
        self.pinNumber = PwmPinNumber
        self.pwm = pigpio.pi()
        self.pwm.set_mode(self.pinNumber, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.pinNumber, 50)
    
    def setPosition(self, deg: int):
        pulsewidth = (deg + 90) / 180 * 2000 + 500
        self.pwm.set_servo_pulsewidth(self.pinNumber, pulsewidth)
    
    def cleanup(self):
        self.pwm.set_PWM_dutycycle(self.pinNumber, 0)
        self.pwm.set_PWM_frequency(self.pinNumber, 0)