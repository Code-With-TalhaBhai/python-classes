


class Segment_Tree:

    def __init__(self,val=None) -> None:
        self.val = val
        self.left = None
        self.right = None


def buildTree1(l,r,arr,i):
    if i >= len(arr):
        return None
    root = Segment_Tree(arr[i])
    mid = (l + r) // 2 
    root.left = buildTree1(l,mid,arr,2*i+1)
    root.right = buildTree1(mid+1,r,arr,2*i+2)
    if root.left is not None and root.right is not None:
        root.val += root.left.val + root.right.val
    return root



def buildTree2(l,r,arr):
    root = Segment_Tree()
    if l == r:
        if not arr:
            return None
        root.val = arr[l]
        return root
        

    mid = (l + r) // 2
    root.left = buildTree2(l,mid,arr)
    root.right = buildTree2(mid+1,r,arr)
    root.val = root.left.val + root.right.val
    return root



def traverse_tree(Node):
    if not Node:
        return None
    
    print(Node.val)
    traverse_tree(Node.left)
    traverse_tree(Node.right)


arr = [3,1,2,7,1]
root1 = buildTree1(0,len(arr),arr,0)
root2 = buildTree2(0,len(arr)-1,arr)
# print(root)
# print(root.val)
# print()
traverse_tree(root1)
print()
traverse_tree(root2)


