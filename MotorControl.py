import config
import RPi.GPIO as GPIO
import time

import Adafruit_MCP4725 as mcp


class MotorControl:

    GPIO.setmode(GPIO.BCM)
    voltage = 0

    dac = mcp.MCP4725(address=0x60)

    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # pin for SPDT switch

    def __init__(self):
        type(self).rpm = 0
        type(self).voltage = 0

    def voltageSet(self):
            for x in range(0, 4097, 150):
                print(x)
                type(self).dac.set_voltage(x)
                time.sleep(2)
        # type(self).dac.set_voltage(type(self).voltage)

    def calculateVoltage(self):
        bore = config.Config.boreSize
        # this will be a list of conditionals of each bore size with the RPM we determine in testing
        print(bore)

    def forward(self):
        GPIO.output(17, GPIO.HIGH)
        while True:
            type(self).voltageSet(self)

    def reverse(self):
        GPIO.output(17, GPIO.LOW)
        while True:
            type(self).voltageSet(self)


motor = MotorControl()
motor.forward()
time.sleep(1)
motor.reverse()
time.sleep(1)


