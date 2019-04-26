#import config
import RPi.GPIO as GPIO
import time

import Adafruit_MCP4725 as mcp

#############################################################################
#############################################################################
#
# This file controls the speed and direction of the Motor.
# The speed is controlled by a 12-bit Digital to Analog converter.
# This DAC is controlled by sending it a raw value.
# The function to calculate the output voltage is:
#         Vout = Vref * Dn/4096
# where Vref is 5V and Dn is the value you input
# For example: 2.5 V = 5 * 2048/4096
# Dn can be changed by sending the function voltageSet a different value.
# This function is called in Forward and Reverse.
#
#############################################################################
#############################################################################


class MotorControl:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)  # pin for SPDT switch
    dac = mcp.MCP4725(address=0x60)

    def __init__(self):
        self.voltage = 0

    def voltageSet(self, voltage):
        type(self).dac.set_voltage(voltage)

    def calculateVoltage(self):
        return
        # bore = config.BORE_SIZE
        # this will be a list of conditionals of each bore size with the RPM we determine in testing

    def forward(self):
        GPIO.output(17, GPIO.LOW)
        type(self).voltageSet(self, 2048)

    def reverse(self):
        return
        # GPIO.output(17, GPIO.HIGH)  # If you ever can go reverse with your brushes uncomment this and remove the
        # type(self).voltageSet(self, 2048)  # return statement

    def Off(self):
        type(self).voltageSet(self, 0)



# motor = MotorControl()
# while True:
#     motor.forward()
#     time.sleep(5)
#     motor.Off()
#     time.sleep(5)


