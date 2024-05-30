from binarytree import root
import copy


root1 = copy.copy(root)
root2 = copy.deepcopy(root)
root2.insert(234)
root2.insert(23)


# root1.Level_Order_Traversal(root1)
# root2.Level_Order_Traversal(root2)



def identical_or_not(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2 or root1.data != root2.data:
        return False

    left = identical_or_not(root1.left,root2.left)
    right = identical_or_not(root1.right,root2.right)

    return left and right



print(identical_or_not(root1,root2))
