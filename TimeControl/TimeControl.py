from Config import config
import time

class TimeControl:

    totalTime = 0
    totalRunTime = 0
    timeRemaining = 0

    def __init__(self):
        type(self).totalTime = 0
        type(self).totalRunTime = 0
        type(self).timeRemaining = 0

    def CalculateTotalTime(self):
        print(config.Config.numCycles) #remove for production
        TimeControl.totalTime = config.Config.numCycles * 24 * 60 # total time for the actuators to rest and run
        TimeControl.totalRunTime = config.Config.numCycles * 8 * 60 #total run time for the actuators

    def Countdown(self):
        type(self).timeRemaining = type(self).totalTime
        while type(self).timeRemaining > 0:
            print(type(self).timeRemaining)
            type(self).timeRemaining = type(self).timeRemaining - 1
            time.sleep(1)
        # do stuff to motor and actuator






time = TimeControl()
time.CalculateTotalTime()