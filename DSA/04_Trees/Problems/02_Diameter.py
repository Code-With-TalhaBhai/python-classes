from binarytree import root


# 1. diameter using nodes
# 2. diameter using edges



def height(root):
    if root == None:
        return 0
    
    left = height(root.left)
    right = height(root.right)

    hei = max(left,right) + 1
    return hei


# Time Complexity(O(n^2)) -> using nodes
def diameter1(root):
    if root == None:
        return 0
    
    left = diameter1(root.left)
    right = diameter1(root.right)
    left_right_height = height(root.left) + height(root.right) + 1
    
    dia = max(left,max(left_right_height,right))
    return dia


# Time Complexity(O(n)) -> using edges
def diameter2(root): 
    def diameter(root):
        if root is None:
            return (-1,-1) # tuple
        
        left = diameter(root.left)
        right = diameter(root.right)

        # hei = max(left[0],right[0]) + 1
        # dia = left[0]+right[0] + 2
        # return (hei,dia)
        return (max(left[0],right[0])+1,left[0]+right[0]+2)
    return diameter(root)[1]


print(diameter1(root))
print(diameter2(root))
