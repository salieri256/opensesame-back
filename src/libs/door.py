from gpiozero.pins.native import NativeFactory
from gpiozero import Servo

factory = NativeFactory()
pig = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000, pin_factory=factory)

def rotate_m90():
    pig.min()

def rotate_0():
    pig.mid()

def rotate_90():
    pig.max()

class Door:
    def lock(self):
        rotate_m90()
        print('lock door')

    def unlock(self):
        rotate_90()
        print('unlock door')

door = Door()

def get_door():
    return door