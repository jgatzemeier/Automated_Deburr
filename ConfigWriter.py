import json
import main
import config

BORE_SIZE = 0.0
SLEEVE_LENGTH = 0.0
NUM_CYCLES = 0
PRESET = ''


def writeJSON():
    print(BORE_SIZE)
    print(SLEEVE_LENGTH)
    print(NUM_CYCLES)

    data = {
        'boreSize': BORE_SIZE,
        'sleeveLength': SLEEVE_LENGTH,
        'numCycles': NUM_CYCLES
    }

    with open('../current.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def readJSON(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            print(key, value)  # remove for production
            if key == 'boreSize':
                BORE_SIZE = value
            if key == 'sleeveLength':
                SLEEVE_LENGTH = value
            if key == 'numCycles':
                NUM_CYCLES = value

        print('boreSize = ', BORE_SIZE)  # remove for production
        print('sleeveLength = ', SLEEVE_LENGTH)
        print('numCycles = ', NUM_CYCLES)


def readPreset():
    if PRESET == '':
        return
    else:
        filename = '../preset/' + PRESET
        readJSON(filename)


def ConfigWriteMain():
    readPreset()
    writeJSON()
    config.Config.configMain()



readJSON('current.json')
app = main.top()
readPreset()

