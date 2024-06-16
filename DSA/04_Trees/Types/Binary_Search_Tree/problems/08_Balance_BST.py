from bst import root


def inorder(root):
    if not root:
        return None
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def balance_bst(root):
    res = []

    def inorder(root):
        if not root:
            return None
    
        inorder(root.left)
        res.append(root)
        inorder(root.right)

    inorder(root)

    
    def build_bst(res):
        if not res:
            return None
        
        mid = int(len(res)/2)
        root = res[mid]

        root.left = build_bst(res[:mid])
        root.right = build_bst(res[mid+1:])

        return root


    
    balance_root = build_bst(res)
    return balance_root


balance_bst_root = balance_bst(root)
inorder(balance_bst_root) # just for check