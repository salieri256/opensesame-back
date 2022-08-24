import os
import time
from src.servo import Servo
from src.sg92r import SG92R

PWM_PORT = int( os.environ['PWM_PORT'] )

class Door:
    def __init__(self, servo: Servo) -> None:
        self.servo = servo

    def lock(self):
        self.servo.setPosition(-90)
        time.sleep(0.3)
        self.servo.setPosition(0)
        print('lock door')

    def unlock(self):
        self.servo.setPosition(90)
        time.sleep(0.3)
        self.servo.setPosition(0)
        print('unlock door')

servo = SG92R(PwmPinNumber=PWM_PORT)
door = Door(servo)

def get_door():
    return door