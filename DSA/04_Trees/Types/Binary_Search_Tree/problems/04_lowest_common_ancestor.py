from bst import root


def lca(root,p,q):
    curr = root

    while curr:
        if (curr.data > p and curr.data < q) or curr.data == p or curr.data == q:
            return curr.data
        elif curr.data > p:
            curr = curr.left
        elif curr.data < p:
            curr = curr.right 


print(lca(root,10,40))