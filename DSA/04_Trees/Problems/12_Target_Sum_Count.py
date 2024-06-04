from binarytree import root

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).



def targetsum_path_count(root,targetSum):
    count = [0]
    def sum_path_3(root,sum):
        if not root:
            return 
        
        sum += root.data
        if sum > targetSum:
            sum = root.data
        
        if sum == targetSum:
            sum = 0
            count[0] += 1
        
        left = sum_path_3(root.left,sum)
        right = sum_path_3(root.right,sum)


    sum_path_3(root,0)
    return count[0]


print(targetsum_path_count(root,145))