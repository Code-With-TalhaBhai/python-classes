from bst import root



def inorder_predecessor_successor1(root):
    res = []
    def inorder(root):
        if not root:
            return None
        
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)

    inorder(root)

    root_index = res.index(root.data)
    if root_index == 0 or len(res) == 1:
        first = None
    else:
        first = res[root_index-1]

    if len(res) == 1:
        second = None
    else:
        second = res[root_index+1]

    return (first,second)



def get_max(root):
    root = root.left
    while root.right:
        root = root.right
    return root



def get_min(root):
    root = root.right
    while root.left:
        root = root.left
    return root


def inorder_predecessor_successor2(root):
    
    predecessor = get_max(root).data;
    successor = get_min(root).data;

    return (predecessor,successor)


print(inorder_predecessor_successor1(root))
print(inorder_predecessor_successor2(root))