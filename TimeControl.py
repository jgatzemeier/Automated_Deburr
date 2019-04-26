from MotorControl import MotorControl
from ActuatorControl import ActuatorControl
import time
import config

#####################################################################################
#####################################################################################
#
#   This file controls the time that the actuators and motor are running.
#   It is responsible for sending signal to the Motor and Actuator to do something.
#
#   This file will need to be updated as follows when new actuators are purchased.
#
#   The function "Countdown Rest" will be obsolete. It can be commented out.
#   The line that calls that function in timeMain will also need to be commented out.
#   In the function "Countdown Run" you will see more comments on how to edit that
#   function. 1 cycle will now be defined as 16 minutes of run time.
#
######################################################################################
######################################################################################


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
        t = 4 * 60 - type(self).actuator.getFullStroke()  # comment this out and uncomment the following line
        # t = 16 * 60 - type(self).actuator.getFullStroke()

        while t > type(self).actuator.getFullStroke():  # This whole loop will be commented out and replaced by below
            if t < (type(self).actuator.getFullStroke() + type(self).actuator.getStrokeTime()):  # Double checks that we will not surpass the duty cycle of the actuator
                break
            t = t - (type(self).actuator.getStrokeTime() * 2)
            type(self).actuator.Actuation()
            if type(self).forward:
                type(self).motor.forward()
            else:
                type(self).motor.reverse()

        type(self).actuator.fullDown()  # This line can be commented out and MOVED to the bottom of timeMain
        t = t - type(self).actuator.getFullStroke()  # This line is can be commented out
        if t == 0:
            type(self).timeRemaining = type(self).timeRemaining - (4 * 60)
            type(self).actuator.Off()
            type(self).motor.Off()
        # while t > 0:
        #     # type(self).actuator.Actuation()  # This replaces the above while loop
            # if type(self).forward:
            #     type(self).motor.forward()
            # else:
            #     type(self).motor.reverse()

            # type(self).actuator.fullDown()  # This line can be commented out and MOVED to the bottom of timeMain
            # t = t - type(self).actuator.getFullStroke()  # This line is can be commented out
            # if t == 0:
            #     type(self).timeRemaining = type(self).timeRemaining - (4 * 60)
            #     type(self).actuator.Off()
            #     type(self).motor.Off()


    def CountdownRest(self):
        t = 12 * 60
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
        # type(self).actuator.fullDown()  # Uncomment this when you upgrade actuators







# time1 = TimeControl()
# TimeControl.CalculateTotalTime()