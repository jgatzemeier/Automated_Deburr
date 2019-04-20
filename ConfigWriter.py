import json
#from config import Config


class ConfigWriter:

    preset = ''
    boreSize = 0.0
    sleeveLength = 0.0
    numCycles = 0

    def __init__(self):
        return

    def writeJSON(self):
        print(type(self).boreSize)
        print(type(self).sleeveLength)
        print(type(self).numCycles)

        data = {
            'boreSize': type(self).boreSize,
            'sleeveLength': type(self).sleeveLength,
            'numCycles': type(self).numCycles
        }

        with open('current.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)


    def readJSON(self, filename):
        with open(filename) as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                print(key, value)  # remove for production
                if key == 'boreSize':
                    type(self).boreSize = value
                if key == 'sleeveLength':
                    type(self).sleeveLength = value
                if key == 'numCycles':
                    type(self).numCycles = value

            print('boreSize = ', type(self).boreSize)  # remove for production
            print('sleeveLength = ', type(self).sleeveLength)
            print('numCycles = ', type(self).numCycles)

            return [type(self).boreSize, type(self).sleeveLength, type(self).numCycles]


    def readPreset(self):
        if type(self).preset == "Preset":
            return
        else:
            filename = 'preset/' + type(self).preset
            type(self).readJSON(self, filename)


    def ConfigWriteMain(self, preset, boreSize, sleeveLength, numCycles):
        type(self).preset = str(preset.get())
        if boreSize.get() == 'Bore Size':
            type(self).boreSize = 0.0
        else:
            type(self).boreSize = float(boreSize.get())

        if sleeveLength.get() == "Sleeve Length":
            type(self).sleeveLength = 0.000
        elif sleeveLength.get() == "3-7/8":
            type(self).sleeveLength = 3.875
        elif sleeveLength.get() == "4":
            type(self).sleeveLength = 4.000
        elif sleeveLength.get() == "4-7/8":
            type(self).sleeveLength = 4.875
        elif sleeveLength.get() == "5":
            type(self).sleeveLength = 5.000
        elif sleeveLength.get() == "7":
            type(self).sleeveLength = 7.000
        elif sleeveLength.get() == "9":
            type(self).sleeveLength = 9.000
        elif sleeveLength.get() == "10-3/4":
            type(self).sleeveLength = 10.750
        elif sleeveLength.get() == "11-3/4":
            type(self).sleeveLength = 11.750

        if numCycles.get() == '':
            type(self).numCycles = 0
        else:
            type(self).numCycles = int(numCycles.get())
        type(self).readPreset(self)
        type(self).writeJSON(self)
        # config = Config()
        # config.configMain()

#
# yeah = ConfigWriter()
# yeah.readJSON('current.json')
# yeah.readPreset()

