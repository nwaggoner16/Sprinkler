import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


class mcp3008(object):
    def __init__(self, channel):
        self.channel = channel
        # create the spi bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        # create the cs (chip select)
        cs = digitalio.DigitalInOut(board.D5)
        # create the mcp object
        mcp = MCP.MCP3008(spi, cs)
        # create an analog input channel on pin 0
        chan_value = AnalogIn(mcp, channel);
        return chan_value

class cap_moisture_sensor(mcp3008):
    def __init__(self, channel):
        self.channel = channel
    def cap_moisture_level(self, channel):
        moisture_level = (super().__init(self.channel)-55936)/-280




"""print('Raw ADC Value: ', chan.value)
print('Moisture Value: ', (chan.value-55936)/-280)"""

"""55936 = 0
28032 = 100
y=-280x +55936"""
