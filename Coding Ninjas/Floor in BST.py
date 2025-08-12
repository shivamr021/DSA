def floorInBST(root, X):
    # Write your Code here.
    floor_val = -1

    while root:
        if root.data == X:
            return root.data
        elif root.data < X:
            floor_val = root.data
            root = root.right
        else:
            root = root.left

    return floor_val
