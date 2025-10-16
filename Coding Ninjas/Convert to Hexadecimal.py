def toHex(num):
    if num >= 0:
        return hex(num)[2:].upper()
    else:
        # Convert negative number to 32-bit two's complement hex
        return hex((1 << 32) + num)[2:].upper()
