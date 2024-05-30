from binarytree import root


def sum_tree_or_not(root):
    def sum_tree(root):
        if not root:
            return [0,True]
        if not root.left and not root.right:
            return [root.data,True]
        
        left = sum_tree(root.left)
        right = sum_tree(root.right)

        if left[1] and right[1] and left[0] + right[0] == root.data:
            return [2*root.data,True]
            # return [left[0] + right[0] + root.data,True]
        else:
            return [root.data,False]
      
    return sum_tree(root)[1]

print(sum_tree_or_not(root))