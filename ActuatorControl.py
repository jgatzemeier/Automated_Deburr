import time

import RPi.GPIO as GPIO

import config


class ActuatorControl:


    GPIO.setmode(GPIO.BOARD)
    strokeLength = 0
    strokeTime = 0
    speed = 1
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 1
    GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 2

    def __init__(self):
        type(self).strokeLength = 0
        type(self).strokeTime = 0

    def calculateStrokeLength(self):
        sleeve = config.Config.sleeveLength
        plateHeight = 1
        strokeLength = 5.4
        
        #use the clearance from the machine to figure this out

    def calculateStrokeTime(self):
        type(self).strokeTime = type(self).strokeLength * type(self).speed


    def goUp(self):
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(32, GPIO.LOW)
        time.sleep(type(self).strokeTime)

    def goDown(self):
        GPIO.output(12, GPIO.LOW)
        GPIO.output(32, GPIO.HIGH)
        time.sleep(type(self).strokeTime)

    def Actuation(self):
        while True:
            type(self).goUp(self)
            type(self).goDown(self)


act = ActuatorControl()
act.calculateStrokeLength()
act.calculateStrokeTime()
act.Actuation()
