import json
from GUI import main

class ConfigWriter:

    boreSize = 0.0
    sleeveLength = 0.0
    numCycles = 0
    presetNum = 0

    def __init__(self):
        type(self).boreSize = 0.0
        type(self).sleeveLength = 0.0
        type(self).numCycles = 0
        type(self).presetNum = 0

    def writeJSON(self):

        data = {
                'boreSize': type(self).boreSize,
                'sleeveLength': type(self).sleeveLength,
                'numCycles': type(self).numCycles
               }

        with open('../current.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4)


    def readJSON(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                print(key, value)  # remove for production
                if key == 'boreSize':
                    ConfigWriter.boreSize = value
                if key == 'sleeveLength':
                    ConfigWriter.sleeveLength = value
                if key == 'numCycles':
                    ConfigWriter.numCycles = value

            print('boreSize = ', ConfigWriter.boreSize)  # remove for production
            print('sleeveLength = ', ConfigWriter.sleeveLength)
            print('numCycles = ', ConfigWriter.numCycles)

    def readPreset(self):
        if ConfigWriter.presetNum == 0:
            return;
        else:
            filename = '../Presets/Preset' + str(ConfigWriter.presetNum)
            ConfigWriter.readJSON(self, filename)


this = ConfigWriter()
ConfigWriter.presetNum = 1
this.readPreset()
this.writeJSON()
