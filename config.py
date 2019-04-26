import json
from TimeControl import TimeControl

BORE_SIZE = None
SLEEVE_LENGTH = None
NUM_CYCLES = None

########################################################################
########################################################################
#
# This file stores the current Bore size, sleeve length, and number of
# cycles to be used for calculations in other modules.
#
########################################################################
########################################################################


class Config:

    boreSize = 0.0
    sleeveLength = 0.0
    numCycles = 0

    def __init__(self):
        type(self).boreSize = 0.0
        type(self).sleeveLength = 0.0
        type(self).numCycles = 0.0

    def readJSON(self):
        global BORE_SIZE
        global SLEEVE_LENGTH
        global NUM_CYCLES
        with open('current.json') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
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