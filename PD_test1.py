import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn


#Analog functions already define direction
analog_in = AnalogIn(board.A0)

#For digital signals we need to specify the direction, for example:
#A0 = DigitalInOut(board.A0)
#A0.direction = Direction.INPUT

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    #print((get_voltage(analog_in),))
    time.sleep(0.1)
    V = get_voltage(analog_in)

    if V>0.6:
        led.value = True
    else:
        led.value = False