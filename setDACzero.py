import Adafruit_MCP4725

dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

dac.set_voltage(0)