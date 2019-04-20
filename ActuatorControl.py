import time

import RPi.GPIO as GPIO

#import config


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
        #type(self).strokeLength = config.SLEEVE_LENGTH
        type(self).strokeTime = 6.5


    def calculateStrokeTime(self):
        type(self).strokeTime = type(self).strokeLength * type(self).speed
        return

    def goUp(self):
        GPIO.output(22, GPIO.LOW)  # actuator 2
        GPIO.output(27, GPIO.HIGH)  # actuator 2
        GPIO.output(23, GPIO.HIGH)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1
        time.sleep(type(self).strokeTime + 2)
        # time.sleep(type(self).strokeTime/2)
        # GPIO.output(27, GPIO.LOW)  # actuator 2
        # time.sleep(.5)
        # GPIO.output(27, GPIO.HIGH)  # actuator 2
        # time.sleep((type(self).strokeTime / 2)-.5)

    def goDown(self):
        GPIO.output(23, GPIO.LOW)  # actuator 1
        GPIO.output(24, GPIO.HIGH)  # actuator 1
        GPIO.output(22, GPIO.HIGH)  # actuator 2
        GPIO.output(27, GPIO.LOW)  # actuator 2

        time.sleep(type(self).strokeTime)
        type(self).Off(self)
        time.sleep(2)
        # time.sleep(type(self).strokeTime/4)
        # GPIO.output(22, GPIO.LOW)  # actuator 2
        # time.sleep(.25)
        # GPIO.output(22, GPIO.HIGH)  # actuator 2
        # # time.sleep((type(self).strokeTime / 4)-.25)
        # # GPIO.output(22, GPIO.LOW)  # actuator 2
        # # time.sleep(.25)
        # # GPIO.output(22, GPIO.HIGH)  # actuator 2
        # #time.sleep((type(self).strokeTime / 2) - .25)
        # # GPIO.output(22, GPIO.LOW)  # actuator 2
        # # time.sleep(.25)
        # # GPIO.output(22, GPIO.HIGH)  # actuator 2
        # time.sleep((type(self).strokeTime / 4))

    def Actuation(self):
        GPIO.output(24, GPIO.LOW)  # actuator 1
        GPIO.output(23, GPIO.HIGH)  # actuator 1
        GPIO.output(27, GPIO.HIGH)  # actuator 2
        GPIO.output(22, GPIO.LOW)  # actuator 2
        time.sleep(23)
        while True:
            type(self).goDown(self)
            type(self).goUp(self)


    def Off(self):
        GPIO.output(23, GPIO.LOW)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1
        GPIO.output(27, GPIO.LOW)  # actuator 2
        GPIO.output(22, GPIO.LOW)  # actuator 2


act = ActuatorControl()
# # act.calculateStrokeLength()
# # act.calculateStrokeTime()
act.Actuation()
