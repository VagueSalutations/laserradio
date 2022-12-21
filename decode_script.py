import math

# 1 = 1, 2 = 0

original_string_to_decode = """
10010
10011
10101
10101
00111
10001
11110
00111
11111
00100
00001
01011
10110
11110
11100
01100
01100
10000
10000
10100
10000
11001
01011
01100
01101
10001
10111
10010
00000
10101
11011
01111
01110
01001
10110
00110
01000
01000
01011
01000
01000
01100
10101
10110
00110
11000
11011
11001
00000
01010
11101
10111
10111
00100
11011
00011
00100
10100
10101
""".replace("\n", "")

print(original_string_to_decode)


original_string_to_decode = original_string_to_decode[:-(len(original_string_to_decode) % 8)]

binary_number = int(original_string_to_decode, 2)
n_bytes = math.ceil(len(original_string_to_decode) / 8)
byte_array = binary_number.to_bytes(n_bytes, "big")
print("")
print(byte_array)
print("")

# for shift in range(8):
#     string_to_decode = original_string_to_decode[shift:(-8-shift)]

#     try:
#         binary_number = int(string_to_decode, 2)
#         n_bytes = math.ceil(len(string_to_decode) / 8)
#         byte_array = binary_number.to_bytes(n_bytes, "big")
#         print(byte_array)

#         decoded_message = byte_array.decode()

#         print(decoded_message)
#     except UnicodeDecodeError:
#         print(f"Failed attempt at shift value of {shift}")

print("Done!")