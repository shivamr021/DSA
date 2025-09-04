def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    res = []

    def toh(n, s, h, d):
        if n == 0:
            return
        toh(n - 1, s, d, h)   
        res.append([s, d]) 
        toh(n - 1, h, s, d)

    toh(n, 1, 2, 3) 
    return res
