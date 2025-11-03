from collections import Counter

def sortByFrequency(n: int, s: str) -> str:
    freq = Counter(s)
    
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    result = ''.join(char * count for char, count in sorted_chars)
    
    return result
