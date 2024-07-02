# Percentage7BitCompressor.py
"""
This module provides an efficient compression algorithm for percentage values (0.00 to 100.99)
with up to two decimal points precision. It compresses each percentage into 2 bytes using 7-bit
data with a flag bit for distinguishing integer and decimal parts.
"""
def pack_percentage(percentage):
    if not (0 <= percentage <= 100.99):
        raise ValueError("Percentage must be between 0.00 and 100.99")

    # Split percentage into integer and decimal parts
    integer_part = int(percentage)
    decimal_part = int((percentage * 100) % 100)

    # Pack integer part with flag 0
    packed_integer = (integer_part & 0x7F) | (0 << 7)

    # Pack decimal part with flag 1
    packed_decimal = (decimal_part & 0x7F) | (1 << 7)

    return bytearray([packed_integer, packed_decimal])

def unpack_percentage(byte_array):
    if len(byte_array) != 2:
        raise ValueError("Byte array must be exactly 2 bytes long")

    # Initialize variables
    integer_part = 0
    decimal_part = 0

    # Unpack each byte
    for byte in byte_array:
        if byte & 0x80:
            # This is the decimal part (flag bit is 1)
            decimal_part = byte & 0x7F
        else:
            # This is the integer part (flag bit is 0)
            integer_part = byte & 0x7F

    return integer_part + decimal_part / 100

# Test the implementation with an example value
percentage = 40.44
packed_data = pack_percentage(percentage)
print(f"Packed Data: {packed_data}")
print(f"Packed Data Size: {len(packed_data)}")
unpacked_percentage = unpack_percentage(packed_data)
print(f"Unpacked Percentage: {unpacked_percentage:.2f}")


