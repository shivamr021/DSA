def isStrobogrammatic(n):
    
    # Write your code here.
    rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    left = 0
    right = len(n) - 1

    while left <= right:
        if n[left] not in rotate_map or n[right] not in rotate_map:
            return False
        if rotate_map[n[left]] != n[right] or rotate_map[n[right]] != n[left]:
            return False
        left += 1
        right -= 1

    return True
