from bst import root
import collections


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



# Return the length of largest bst subtree
def isValidBst(root,min_range,max_range):
        if not root:
            return True
        
        if root.data < min_range or root.data > max_range:
            return False
        
        
        return isValidBst(root.left,min_range,root.data) and isValidBst(root.right,root.data,max_range)



# Time-Complexity(O(N^2))
def largest_subtree_bst1(root):
    if not root:
        return 1
    
    left = largest_subtree_bst1(root.left)
    right = largest_subtree_bst1(root.right)

    if isValidBst(root,float("-inf"),float("inf")):
        return max(left,right) + 1
    # else:
    #     return max(left,right) + 1 
    


def largest_subtree_bst2(root):
    ... 



print(largest_subtree_bst1(root))
# print(largest_subtree_bst2(root))
