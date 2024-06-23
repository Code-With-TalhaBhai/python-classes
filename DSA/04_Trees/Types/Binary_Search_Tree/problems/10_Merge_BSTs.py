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




def merge_bsts(total_inorder):

    all_inorders = []
    for inorder in total_inorder:
        all_inorders += inorder  
    all_inorders.sort()

    
    # building tree from inorder
    def build_bsts(inorder):
        if not inorder:
            return None
        
        mid = int(len(inorder)/2)
        root = BST(inorder[mid])

        root.left = build_bsts(inorder[:mid])
        root.right = build_bsts(inorder[mid+1:])

        return root
    
    return build_bsts(all_inorders)



merge_root = merge_bsts(total_inorder)
level_order_traversal(merge_root)

