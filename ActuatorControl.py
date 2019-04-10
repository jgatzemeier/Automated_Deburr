import time

import RPi.GPIO as GPIO


import config


class ActuatorControl:



    strokeLength = 0
    strokeTime = 15
    speed = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 1 hot
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  #pin for relay 1 cold

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
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        time.sleep(10)#type(self).strokeTime)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

    def goDown(self):
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(10)#type(self).strokeTime)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

    def Actuation(self):
       while True:
            type(self).goUp(self)
            type(self).goDown(self)



act = ActuatorControl()
act.calculateStrokeLength()
act.calculateStrokeTime()
act.Actuation()
