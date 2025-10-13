def sortZeroesAndOne(arr, n):
    low = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]  # swap 0 to the front
            low += 1
