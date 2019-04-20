import json
from TimeControl import TimeControl

BORE_SIZE = None
SLEEVE_LENGTH = None
NUM_CYCLES = None

class Config:

    boreSize = 0.0
    sleeveLength = 0.0
    numCycles = 0


    def __init__(self):
        global BORE_SIZE
        global SLEEVE_LENGTH
        global NUM_CYCLES
        type(self).boreSize = 0.0
        type(self).sleeveLength = 0.0
        type(self).numCycles = 0.0


    def readJSON(self):

        with open('current.json') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                print(key, value) #remove for production
                if key == 'boreSize':
                    BORE_SIZE = value
                if key == 'sleeveLength':
                    SLEEVE_LENGTH = value
                if key == 'numCycles':
                    NUM_CYCLES = value


    def configMain(self):
        type(self).readJSON(self)
        timeControl = TimeControl()
        timeControl.timeMain()


# app = Config()
# Config.readJSON(app)