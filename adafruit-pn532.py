# pip3 install adafruit-circuitpython-pn532
# pip install adafruit-blinka
# SPI

# assign reset pin to digital pin D6 on board
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

uid = pn532.read_passive_target(timeout=0.5)