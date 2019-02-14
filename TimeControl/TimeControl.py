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
        TimeControl.totalTime = config.Config.numCycles * 32 * 60 # total time for the actuators to rest and run
        TimeControl.totalRunTime = config.Config.numCycles * 8 * 60 #total run time for the actuators

    def CountdownRun(self):
        t = 8 * 60
        while t > 0:
            t = t - 1
            time.sleep(1)
        if t == 0:
            type(self).timeRemaining = type(self).timeRemaining - (8 * 60)
            # tell motor and actuator to stop

    def CountdownRest(self):
        t = 24 * 60
        while t > 0:
            t = t - 1
            time.sleep(1)
        if t == 0:
            type(self).timeRemaining = type(self).timeRemaining - (24 * 60)
            # tell motor and actuator to start




time = TimeControl()
time.CalculateTotalTime()