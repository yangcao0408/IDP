import network
import struct # This module converts between Python values and C structs represented as Python bytes objects.
import time
import machine

# NOTE INCORRECT CONNECTIONS WILL DESTROY THE SENSOR. CHECK WITH BENCH MULTIMETER BEFORE POWER/USE
# Red---3v3
# Black---ground
# Blue---sda
# Yellow---scl

# The code reader has the I2C ID of hex 0c, or decimal 12.
TINY_CODE_READER_I2C_ADDRESS = 0x0C

TINY_CODE_READER_DELAY = 0.05 #How long to pause between sensor polls.
TINY_CODE_READER_LENGTH_OFFSET = 0
TINY_CODE_READER_LENGTH_FORMAT = "H"
TINY_CODE_READER_MESSAGE_OFFSET = TINY_CODE_READER_LENGTH_OFFSET + struct.calcsize(TINY_CODE_READER_LENGTH_FORMAT)
TINY_CODE_READER_MESSAGE_SIZE = 254
TINY_CODE_READER_MESSAGE_FORMAT = "B" * TINY_CODE_READER_MESSAGE_SIZE
TINY_CODE_READER_I2C_FORMAT = TINY_CODE_READER_LENGTH_FORMAT + TINY_CODE_READER_MESSAGE_FORMAT
TINY_CODE_READER_I2C_BYTE_COUNT = struct.calcsize(TINY_CODE_READER_I2C_FORMAT)

i2c = machine.I2C(1, scl=machine.Pin(19), sda=machine.Pin(18), freq=400000)

def scan_for_QR(trytime):
  #This function scans for a QR code for trytime long and at the end will return the final instance of QR code it was able to scan
  start_time = time.time()
  code = 0
  #If final code is returned as 0 then nothing was scanned

  while time.time() - start_time < trytime:
    sleep(TINY_CODE_READER_DELAY)
    read_data = i2c.readfrom(TINY_CODE_READER_I2C_ADDRESS, TINY_CODE_READER_I2C_BYTE_COUNT)
    
    message_length, = struct.unpack_from(TINY_CODE_READER_LENGTH_FORMAT, read_data,TINY_CODE_READER_LENGTH_OFFSET)
    message_bytes = struct.unpack_from(TINY_CODE_READER_MESSAGE_FORMAT, read_data, TINY_CODE_READER_MESSAGE_OFFSET)

    if message_length != 0:
      message_string = bytearray(message_bytes[0:message_length]).decode("utf-8")
      code = message_string[0]
  
  return code
