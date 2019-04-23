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
        self.strokeLength = config.SLEEVE_LENGTH
        self.calculateStrokeTime()
        self.fullStroke = 23
        type(self).Off(self)

    def getStrokeTime(self):
        return self.strokeTime

    def getFullStroke(self):
        return self.fullStroke

    def calculateStrokeTime(self):
        self.strokeTime = self.strokeLength * type(self).speed + 1
        return

    def goUp(self):
        GPIO.output(22, GPIO.LOW)  # actuator 2
        GPIO.output(27, GPIO.HIGH)  # actuator 2
        GPIO.output(23, GPIO.HIGH)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1
        time.sleep(self.strokeTime)
        # time.sleep(type(self).strokeTime/2)
        # GPIO.output(27, GPIO.LOW)  # actuator 2
        # time.sleep(.5)
        # GPIO.output(27, GPIO.HIGH)  # actuator 2
        # time.sleep((type(self).strokeTime / 2)-.5)

    def goDown(self):
        GPIO.output(27, GPIO.LOW)  # actuator 2
        GPIO.output(22, GPIO.HIGH)  # actuator 2
        GPIO.output(24, GPIO.HIGH)  # actuator 1
        GPIO.output(23, GPIO.LOW)  # actuator 1


        time.sleep(self.strokeTime - 1)
        type(self).Off(self)
        time.sleep(1)
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
        type(self).goDown(self)
        type(self).goUp(self)

    def fullUp(self):
        GPIO.output(22, GPIO.LOW)  # actuator 2
        GPIO.output(27, GPIO.HIGH)  # actuator 2
        GPIO.output(23, GPIO.HIGH)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1

        time.sleep(self.fullStroke)
        type(self).Off(self)

    def fullDown(self):

        GPIO.output(27, GPIO.LOW)  # actuator 2
        GPIO.output(22, GPIO.HIGH)  # actuator 2
        GPIO.output(24, GPIO.HIGH)  # actuator 1
        GPIO.output(23, GPIO.LOW)  # actuator 1

        time.sleep(self.fullStroke)
        type(self).Off(self)


    def Off(self):
        GPIO.output(23, GPIO.LOW)  # actuator 1
        GPIO.output(24, GPIO.LOW)  # actuator 1
        GPIO.output(27, GPIO.LOW)  # actuator 2
        GPIO.output(22, GPIO.LOW)  # actuator 2
#
# #
# act = ActuatorControl()
# # # act.calculateStrokeLength()
# # # act.calculateStrokeTime()
# act.fullDown()
# # act.Actuation()
