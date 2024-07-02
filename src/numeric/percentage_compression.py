import zlib
import struct

# Example list of integers
integer_data = [50, 55, 60, 65, 70]

# Example single integer
single_integer = 12345

# Convert the single integer to bytes (4-byte integer in little-endian order)
byte_data_single = struct.pack('i', single_integer)
byte_array_single = bytearray(byte_data_single)
print(f"Byte Array from Single Integer: {byte_array_single}")


# Convert integers to bytes
# This depends on the range of integers you have. For simplicity, here we assume 1-byte integers.
byte_data = bytearray(integer_data)
print(f"byte_data : {byte_data}")

# Convert integers to bytes assuming 4 bytes per integer
byte_data = b''.join(struct.pack('i', num) for num in integer_data)
print(f"Byte Array Representation: {byte_data}")

# Get original size in bytes
original_size = len(byte_data)

# Compress the byte data
compressed_data = zlib.compress(byte_data)
print(f"Compressed Data: {compressed_data}")

# Get compressed size in bytes
compressed_size = len(compressed_data)

# Calculate compression ratio
compression_ratio = original_size / compressed_size

print(f"Original Data Size: {original_size} bytes")
print(f"Compressed Data Size: {compressed_size} bytes")
print(f"Compression Ratio: {compression_ratio:.2f}")

# Decompress the data
decompressed_byte_data = zlib.decompress(compressed_data)
print(f"Decompressed Byte Data: {decompressed_byte_data}")

# Convert bytes back to integers
# Again, this depends on the original integer size used for conversion.
decompressed_data = list(decompressed_byte_data)
print(f"Decompressed Integers: {decompressed_data}")


def percentage_compression(data):

    return 1

