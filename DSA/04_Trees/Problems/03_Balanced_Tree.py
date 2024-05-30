from binarytree import root


def balancedOrNot(root):

    def balance(root):
        if root is None:
            return [-1,True]
        
        left = balance(root.left)
        right = balance(root.right)
        
        height = max(left[0],right[0])+1

        balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
        return [height,balanced]

        # OR
        # if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
        #     return [height,True]
        # else:
        #     return [height,False]
    return balance(root)[1]

print(balancedOrNot(root))