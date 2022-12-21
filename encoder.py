
from machine import Pin
import time

testdata = "1010101010101010101010101010101010101010101010101010101010101"
testbaud = 1

data = "Hello World!"
baud = 9600


# Initialize onboard LED pins
led1 = Pin(8, Pin.OUT)
led2 = Pin(9, Pin.OUT)
led3 = Pin(10, Pin.OUT)
led4 = Pin(11, Pin.OUT)
led5 = Pin(12, Pin.OUT)
leds = [led1, led2, led3, led4, led5]
# Initialize laser pin
Tx = Pin(1, Pin.OUT)
Tx_enable = Pin(2, Pin.OUT)


# Convert string into list of bytes
bytes = []
for chr in data:
    # chr > ordinal (ASCII) > binary string
    # Leading 0b of bin() string clipped and padded with 0s to 8 bits 
    bytes.append('{:0>8}'.format(bin(ord(chr))[2:]))

# Convert byte list into a single string
bytestring = ''.join(bytes)

"""
Tx_enable.off()
while True:
    for led in leds:
        led.toggle()
    Tx.toggle()
    time.sleep(1)
"""

Tx_enable.on()

for idx, bit in enumerate(testdata):
    
    # Extract data and update the pin dipslay
    if idx < len(testdata)-5:
        i = idx+5
        for led in leds:
            if testdata[i] == '1':
                led.on()
            else:
                led.off()
            i -= 1

    # Command laser
    if bit == '1':
        Tx.on()
    else:
        Tx.off()
    
    # Delay by baud rate
    time.sleep(1.0/testbaud)


