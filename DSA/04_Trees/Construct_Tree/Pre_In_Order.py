from tree_check import check_preOrder,check_inOrder

class Tree:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right



def buildTree(preOrder,inOrder):
    if not preOrder or not inOrder:
        return None
    
    root = Tree(preOrder[0])
    root_index = inOrder.index(root.data)
    # root_index = inOrder.index(root)

    root.left = buildTree(preOrder[1:root_index+1],inOrder[:root_index])
    root.right = buildTree(preOrder[root_index+1:],inOrder[root_index+1:])
    return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = buildTree(preorder,inorder)

print(f"Matching PreOrder {check_preOrder(root)}")
print(f"Matching InOrder {check_inOrder(root)}")





