### try programming the rfid chips to specific things

# pip3 install adafruit-circuitpython-pn532
# pip install adafruit-blinka
# SPI

import board
import busio
import time

from digitalio import DigitalInOut
from adafruit_pn532.spi import PN532_SPI

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs_pin = DigitalInOut(board.D5)
pn532 = PN532_SPI(spi, cs_pin, debug=False)

ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

pn532.SAM_configuration()
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    print(".", end="")
    if uid is not None:
        break

# convert read to number 
