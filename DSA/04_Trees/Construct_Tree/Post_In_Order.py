from tree_check import check_postOrder,check_inOrder

class Tree:
    def __init__(self,data=0,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right



def buildTree1(postOrder,inOrder):
    if not postOrder or not inOrder:
        return None
    
    root = Tree(postOrder[-1])
    root_index = inOrder.index(root.data)
    postOrder.pop() # different from pre-order

    root.left = buildTree1(postOrder[:root_index],inOrder[:root_index])
    root.right = buildTree1(postOrder[root_index:],inOrder[root_index+1:])
    return root



def buildTree2(postOrder,inOrder):
    if not inOrder:
        return None
    
    root = Tree(postOrder.pop())
    root_index = inOrder.index(root.data)

    root.right = buildTree2(postOrder,inOrder[root_index+1:])
    root.left = buildTree2(postOrder,inOrder[:root_index])
    return root



postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]


# root = buildTree1(postorder,inorder)
root = buildTree2(postorder,inorder)

print(f"Matching PreOrder {check_postOrder(root)}")
print(f"Matching InOrder {check_inOrder(root)}")