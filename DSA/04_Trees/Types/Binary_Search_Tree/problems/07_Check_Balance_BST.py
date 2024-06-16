from bst import root



def check_balance_bst(root):
    if not root:
        return (0,True)

    left =  check_balance_bst(root.left) 
    right = check_balance_bst(root.right)

    height = max(left[0],right[0]) + 1

    if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
        return (height,True)
    else:
        return (height,False)






print(check_balance_bst(root)[1])