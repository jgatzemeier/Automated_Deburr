import json

class Config:

    boreSize = 0.0
    sleeveLength = 0.0
    numCycles = 0


    def __init__(self):
        return
        #type(self).boreSize = 0.0
        #type(self).sleeveLength = 0.0
        #type(self).numCycles = 0.0


    def readJSON(self):
        with open('current.json') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                print(key, value) #remove for production
                if key == 'boreSize':
                    Config.boreSize = value
                if key == 'sleeveLength':
                    Config.sleeveLength = value
                if key == 'numCycles':
                    Config.numCycles = value

            print('boreSize = ', Config.boreSize) #remove for production
            print('sleeveLength = ', Config.sleeveLength)
            print('numCycles = ', Config.numCycles)


app = Config()
Config.readJSON(app)