import collections
from bst import BST

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

# Two BSTs
total_inorder = [
    [1,3,5],[2,4,6]
]

all_inorders = []
for inorder in total_inorder:
    all_inorders += inorder    
all_inorders.sort()



def merge_bsts(inorder):
    if not inorder:
        return None
    
    mid = int(len(inorder)/2)
    root = BST(inorder[mid])

    root.left = merge_bsts(inorder[:mid])
    root.right = merge_bsts(inorder[mid+1:])

    return root



merge_root = merge_bsts(all_inorders)
level_order_traversal(merge_root)

