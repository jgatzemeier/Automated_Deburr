import config
import RPi.GPIO as GPIO
import time

# import Adafruit_MCP4725 as mcp
# import smbus
#import quick2wire.i2c as i2c

class MotorControl:

    GPIO.setmode(GPIO.BCM)
    voltage = 0

    # dac = mcp.MCP4725(address=0x61)


    # # I2C channel 1 is connected to the GPIO pins
    # channel = 1
    # #
    # # #  MCP4725 defaults to address 0x60
    # address = 0x61
    # #
    # # # Register addresses (with "normal mode" power-down bits)
    # reg_write_dac = 0x40
    # #
    # # # Initialize I2C (SMBus)
    # bus = smbus.SMBus(1)


    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # pin for SPDT switch

    def __init__(self):
        type(self).rpm = 0
        type(self).voltage = 0

    def voltageSet(self, voltage):
        return

            # for x in range(0, 4097, 150):
            #     print(x)
            #     type(self).dac.set_voltage(x)
            #     time.sleep(2)

            # Create a sawtooth wave 16 times
        # for i in range(0x10000):
        #     # Create our 12-bit number representing relative voltage
        #     voltage = i & 0xfff
        #
        #     # Shift everything left by 4 bits and separate bytes
        #     msg = (voltage & 0xff0) >> 4
        #     msg = [msg, (msg & 0xf) << 4]
        #
        #      # Write out I2C command: address, reg_write_dac, msg[0], msg[1]
        #     type(self).bus.write_i2c_block_data(type(self).address, type(self).reg_write_dac, msg)


    def calculateVoltage(self):
        bore = config.BORE_SIZE
        # this will be a list of conditionals of each bore size with the RPM we determine in testing
        print(bore)

    def forward(self):
        GPIO.output(17, GPIO.HIGH)
        while True:
            type(self).voltageSet(self, 100)

    def reverse(self):
        GPIO.output(17, GPIO.LOW)
        while True:
            type(self).voltageSet(self, 100)

    def Off(self):
        type(self).voltageSet(self, 0)


motor = MotorControl()
motor.forward()
# time.sleep(1)
# motor.reverse()
# time.sleep(1)


