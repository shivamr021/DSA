from collections import Counter
def amazingStrings(first, second, third):
    # Write your code here
    combined = first + second
    count_combined = Counter(combined)
    count_third = Counter(third)

    # Return a string 'YES' or 'NO' denoting the answer
    if count_combined == count_third:
        return "YES"
    else:
        return "NO"
