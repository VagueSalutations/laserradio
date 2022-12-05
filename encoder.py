
import time

data = "Hello World!"
baud = 9600

# Convert string into list of bytes
bytes = []
for chr in data:
    # chr > ordinal (ASCII) > binary string
    # Leading 0b of bin() string clipped and padded with 0s to 8 bits 
    bytes.append('{:0>8}'.format(bin(ord(chr))[2:]))

# Convert byte list into a single string
bytestring = ''.join(bytes)

"""
for bit in bytestring:
    if bit == '1':
        # Hold GPIO high
    else:
        # Hold GPIO low
    time.sleep(1.0/baud)
"""