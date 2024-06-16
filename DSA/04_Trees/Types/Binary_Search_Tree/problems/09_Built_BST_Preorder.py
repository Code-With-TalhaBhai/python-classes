import collections

class bst:
    def __init__(self,data=0)->None:
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return None
    
    dq = collections.deque()
    dq.append(root)
    res = []

    while dq:
        level = []
        for i in range(len(dq)):
            curr = dq.popleft()

            left = curr.left
            right = curr.right

            if left:
                dq.append(left)
            if right:
                dq.append(right)

            level.append(curr.data)
        res.append(level)
    print(res)


# Time-Complexity of O(n^2)
def build_bst1(preorder):
    root = bst(preorder[0])

    def insert(root,data):
        if data < root.data:
            if root.left == None:
                root.left = bst(data)
            else:
                insert(root.left,data)

        elif data > root.data:
            if root.right == None:
                root.right = bst(data)
            else:
                insert(root.right,data)

    for i in range(1,len(preorder)):
        insert(root,preorder[i])

    return root


def build_bst2(preorder):
    inorder = sorted(preorder) #sorted form of preorders

    def build_tree(preorder,inorder):
        if not inorder or not preorder:
            return None
        
        root = bst(preorder[0])
        root_index = inorder.index(root.data)

        root.left = build_tree(preorder[1:root_index+1],inorder[:root_index]) # type: ignore
        root.right = build_tree(preorder[root_index+1:],inorder[root_index+1:]) # type: ignore
        return root

    return build_tree(preorder,inorder)



def build_bst3(preorder):
    root = bst(preorder[0])
    stack = []
    stack.append(root)

    for i in range(1,len(preorder)):
        if preorder[i] < stack[-1].data:
            stack[-1].left = bst(preorder[i])
            stack.append(stack[-1].left)
        else:
            while stack and preorder[i] > stack[-1].data:
                node = stack.pop()
            node.right = bst(preorder[i])
            stack.append(node.right)

    return root
    
    


preorder = [50,25,10,30,40,70,60]
root1 = build_bst1(preorder)
level_order_traversal(root1)

root2 = build_bst2(preorder)
level_order_traversal(root2)

root3 = build_bst3(preorder)
level_order_traversal(root3)