from MotorControl import MotorControl
from ActuatorControl import ActuatorControl
import time
import config



class TimeControl:

    totalTime = 0
    totalRunTime = 0
    timeRemaining = 0
    forward = True
    actuator = None
    motor = None

    def __init__(self):
        type(self).totalTime = 0
        type(self).totalRunTime = 0
        type(self).timeRemaining = 0
        type(self).actuator = ActuatorControl()
        type(self).motor = MotorControl()

    # def CalculateTotalTime(self):
    #     print(config.NUM_CYCLES) #remove for production
    #     type(self).totalTime = config.NUM_CYCLES * 32 * 60 # total time for the actuators to rest and run
    #     type(self).totalRunTime = config.NUM_CYCLES * 8 * 60 #total run time for the actuators

    def CountdownRun(self):
        type(self).actuator.fullUp()
        t = 8 * 60 - type(self).actuator.getFullStroke()

        while t > type(self).actuator.getFullStroke():
            if t < (type(self).actuator.getFullStroke() + type(self).actuator.getStrokeTime()):  # Double checks that we will not surpass the duty cycle of the actuator
                break
            t = t - (type(self).actuator.getStrokeTime() * 2)
            type(self).actuator.Actuation()
            if type(self).forward:
                type(self).motor.forward()
            else:
                type(self).motor.reverse()

        type(self).actuator.fullDown()
        t = t - type(self).actuator.getFullStroke()
        if t == 0:
            type(self).timeRemaining = type(self).timeRemaining - (4 * 60)
            type(self).actuator.Off()
            type(self).motor.Off()


    def CountdownRest(self):
        t = 24 * 60
        while t > 0:
            t = t - 1
            time.sleep(1)
        if t == 0:
            type(self).timeRemaining = type(self).timeRemaining - (12 * 60)
            if type(self).forward:
                type(self).forward = False
            else:
                type(self).forward = True

    def timeMain(self):
        # type(self).CalculateTotalTime(self)

        cycles = config.NUM_CYCLES
        while cycles > 0:
            type(self).CountdownRun(self)
            type(self).CountdownRest(self)
            cycles = cycles - 1







# time1 = TimeControl()
# TimeControl.CalculateTotalTime()