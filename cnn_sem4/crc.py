def crc_remainder(data, divisor):
    # Append the necessary number of zeroes to the data
    data += '0' * (len(divisor) - 1)
    data = list(data)
    divisor = list(divisor)
    divisor_length = len(divisor)
    # Perform division
    for i in range(len(data) - divisor_length + 1):
        # If the leftmost bit is 0, perform bitwise XOR with 0s
        if data[i] == '0':
            continue
        # Perform bitwise XOR between data and divisor
        for j in range(divisor_length):
            data[i + j] = str(int(data[i + j]) ^ int(divisor[j]))
    # The remainder is the leftover data after division
    remainder = ''.join(data)[-divisor_length + 1:]
    return remainder

def crc_encode(data, divisor):
    remainder = crc_remainder(data, divisor)
    # Append the remainder to the original data
    encoded_data = data + remainder
    return encoded_data

def crc_check(data, divisor):
    remainder = crc_remainder(data, divisor)
    # If remainder is all zeroes, no error
    if remainder == '0' * (len(divisor) - 1):
        return True
    else:
        return False

# Example usage:
data = "11010011101100"
divisor = "1011"

encoded_data = crc_encode(data, divisor)
print("Encoded data with CRC:", encoded_data)

# Introducing an error
corrupted_data = "11010111101100"
# Check if there's an error
is_error = crc_check(corrupted_data, divisor)
if is_error:
    print("No error detected.")
else:
    print("Error detected.")
