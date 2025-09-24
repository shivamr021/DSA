def findSetBit(N):
    return -1 if N == 0 or (N & (N - 1)) != 0 else N.bit_length()
