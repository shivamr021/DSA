from collections import Counter

def slotScore(original, guess):
    points = 0
    # Lists to store unmatched colors after perfect hits
    unmatched_original = []
    unmatched_guess = []
    
    # Step 1: Find perfect hits
    for o, g in zip(original, guess):
        if o == g:
            points += 2
        else:
            unmatched_original.append(o)
            unmatched_guess.append(g)
    
    # Step 2: Count pseudo hits
    count_original = Counter(unmatched_original)
    
    for g in unmatched_guess:
        if count_original[g] > 0:
            points += 1
            count_original[g] -= 1  # consume one occurrence
    
    return points
