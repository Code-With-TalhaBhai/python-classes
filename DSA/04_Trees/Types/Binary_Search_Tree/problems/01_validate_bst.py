from bst import root


def validate_bst1(root):
    def valid_bst(root,min,max):
        if not root:
            return True

        if not (root.data > min and root.data < max):
            return False

        return valid_bst(root.left,min,root.data) and valid_bst(root.right,root.data,max)

    # "-inf" ----> "Negative Infinity"
    # "inf" -----> "Postive Infinity"
    return valid_bst(root,float("-inf"),float("inf"))


def validate_bst2(root):
    res = []
    def inorder(root):
        if not root:
            return None
        
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)

    inorder(root)

    temp = res[0]
    for i in range(1,len(res)):
        if temp >= res[i]:
            return False
        temp = res[i]

    return True




print(validate_bst1(root))
print(validate_bst2(root)) # Do In-order traversal,check it is sorted or not