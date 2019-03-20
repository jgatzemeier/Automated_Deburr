import config
import RPi.GPIO as GPIO
import time

# Import the MCP4725 module.
import board
import busio

import adafruit_mcp4725



class MotorControl:

    GPIO.setmode(GPIO.BOARD)
    rpm = 0
    voltage = 0

    # Initialize I2C bus.
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize MCP4725.
    dac = adafruit_mcp4725.MCP4725(i2c)
    # Optionally you can specify a different addres if you override the A0 pin.
    # amp = adafruit_max9744.MAX9744(i2c, address=0x63)

    GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW) #pin for SPDT switch


    def __init__(self):
        type(self).rpm = 0
        type(self).voltage = 0

    def voltageSet(self):
        while True:
            print('Going up 0-3.3V...')
            for i in range(2048):
                type(self).dac.raw_value = i
            # Go back down the 12-bit raw range.
            print('Going down 3.3-0V...')
            for i in range(2048, -1, -1):
                type(self).dac.raw_value = i

    def calculateRPM(self):
        bore = config.Config.boreSize
        # this will be a list of conditionals of each bore size with the RPM we determine in testing
        print(bore)

    def calculateVoltage(self):
        return

    def forward(self):
        GPIO.output(1, GPIO.HIGH)
        type(self).voltageSet(self)

    def reverse(self):
        GPIO.output(1, GPIO.LOW)
        type(self).voltageSet(self)



