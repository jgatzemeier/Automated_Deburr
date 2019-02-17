import RPi.GPIO as GPIO
from Config import config
import time

class ActuatorControl:


    GPIO.setmode(GPIO.BOARD)
    strokeLength = 0
    strokeTime = 0
    speed = 0

    GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 1
    GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 2

    def __init__(self):
        type(self).strokeLength = 0
        type(self).strokeTime = 0

    def calculateStrokeLength(self):
        sleeve = config.Config.sleeveLength
        #use the clearance and shit from the machine to figure this out

    def calculateStrokeTime(self):
        type(self).strokeTime = type(self).strokeLength * type(self).speed


    def goUp(self):
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        time.sleep(type(self).strokeTime)

    def goDown(self):
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        time.sleep(type(self).strokeTime)

    def Acuation(self):
        while True:
            type(self).goUp()
            type(self).goDown()
