import config
import RPi.GPIO as GPIO
import spidev

class MotorControl:

    GPIO.setmode(GPIO.BOARD)
    rpm = 0
    voltage = 0

    GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW) #pins for SPDT switch
    GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)


    def __init__(self):
        type(self).rpm = 0
        type(self).voltage = 0

    def calculateRPM(self):
        bore = config.Config.boreSize
        # this will be a list of conditionals of each bore size with the RPM we determine in testing
        print(bore)

    def calculateVoltage(self):
        return

    def forward(self):
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.LOW)

        #I2C FOR VOLTAGE

    def reverse(self):
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.HIGH)

        #I2C FOR VOLTAGE

    def brake(self):
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        #I2C FOR VOLTAGE
