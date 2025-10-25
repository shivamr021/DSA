from sys import stdin

def highestOccuringChar(string):
    if not string:
        return ''
    
    freq = [0] * 26  

    for ch in string:
        index = ord(ch) - ord('a')
        freq[index] += 1

    max_freq = 0
    max_char_index = 0
    for i in range(26):
        if freq[i] > max_freq:
            max_freq = freq[i]
            max_char_index = i

    return chr(max_char_index + ord('a'))

# Main
string = stdin.readline().strip()
ans = highestOccuringChar(string)
print(ans)
