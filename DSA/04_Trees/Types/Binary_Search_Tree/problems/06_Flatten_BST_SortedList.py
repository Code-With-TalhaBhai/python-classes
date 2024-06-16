from bst import root


def flattenBST(root):

    res = []
    curr = root

    # In-order traversal by morris traversal
    while curr:
        if curr.left is None:
            res.append(curr)
            curr = curr.right   
        else:
            predecessor = curr.left
            while predecessor.right:
                predecessor = predecessor.right
            
            predecessor.right = curr
            temp = curr
            curr = curr.left
            temp.left = None

    temp = res[0]
    for i in range(1,len(res)):
        temp.right = res[i]
        temp = temp.right
    temp.right = None

    return res[0]


def traverse_linkedlist(root):

    while root:
        print(root.data,end=" ")
        root = root.right
    print()


linkedlist_root = flattenBST(root)
traverse_linkedlist(linkedlist_root)
# traverse_linkedlist(root)