def reverseString(s: str) -> str:
    # Write your code from here.
    words = s.split()

    return " ".join(reversed(words))
