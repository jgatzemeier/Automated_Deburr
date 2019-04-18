import time

import RPi.GPIO as GPIO


import config


class ActuatorControl:

    strokeLength = 0
    strokeTime = 0
    speed = .3
    '''
        NOTE: Pin layout can be found at pinout.xyz
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)  # pin for actuator 1 hot
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  # pin for actuator 1 cold
    GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)  # pin for actuator 2 hot
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  # pin for actuator 2 cold

    def __init__(self):
        type(self).strokeLength = 0
        type(self).strokeTime = 20

    def calculateStrokeLength(self):
        sleeve = config.Config.sleeveLength
        plateHeight = 1
        strokeLength = 0
        if sleeve == 3.875:
            strokeLength = 0
        elif sleeve == 4.875:
            strokeLength = 0
        elif sleeve = 5.000:
            strokeLength = 0
        elif sleeve = 7.000:
            strokeLength = 0
        elif sleeve = 9.000:
            strokeLength = 0
        elif sleeve = 10.750:
            strokeLength = 0
        elif sleeve = 11.750:
            strokeLength = 0
        else:
            strokeLength = 0

        type(self).strokeLength = strokeLength

    def calculateStrokeTime(self):
        type(self).strokeTime = type(self).strokeLength * type(self).speed
        return

    def goUp(self):
        GPIO.output(23, GPIO.HIGH)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1
        GPIO.output(27, GPIO.HIGH)  # actuator 2
        GPIO.output(22, GPIO.LOW)  # actuator 2
        time.sleep(type(self).strokeTime)

    def goDown(self):
        GPIO.output(23, GPIO.LOW)  # actuator 1
        GPIO.output(24, GPIO.HIGH)  # actuator 1
        GPIO.output(27, GPIO.LOW)  # actuator 2
        GPIO.output(22, GPIO.HIGH)  # actuator 2
        time.sleep(type(self).strokeTime)

    def Actuation(self):
       while True:
            type(self).goUp(self)
            type(self).goDown(self)


act = ActuatorControl()
act.calculateStrokeLength()
act.calculateStrokeTime()
act.Actuation()
