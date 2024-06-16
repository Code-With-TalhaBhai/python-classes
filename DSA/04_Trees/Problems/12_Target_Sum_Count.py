from itertools import count
from binarytree import root

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


# Two functions are being used Time-Complexity of O(n^2)
def targetsum_path_count1(root,targetSum):
    count = [0]

    def path_count(root,sum):
        if not root:
            return None
        
        sum += root.data

        if sum == targetSum:
            count[0] += 1
        
        path_count(root.left,sum)
        path_count(root.right,sum)


    def sum_path_3(root):
        if not root:
            return None
        
        path_count(root,0)

        sum_path_3(root.left)
        sum_path_3(root.right)

    sum_path_3(root)
    return count[0]

    



# def targetsum_path_count2(root,targetSum):
#     paths_sum = {0:1}
#     count = [0]

#     def sub_paths(root,acc_sum):
#         if not root:
#             return None
        
#         acc_sum += root.data

#         diff = acc_sum - targetSum

#         if diff in paths_sum:
#             count[0] += paths_sum[diff]
#         if acc_sum not in paths_sum:
#             paths_sum[acc_sum] = 1
#         else:
#             paths_sum[acc_sum] += 1
    
#         sub_paths(root.left,acc_sum)
#         sub_paths(root.right,acc_sum)

#     sub_paths(root,0)
#     print(paths_sum)
#     return count[0]


def targetsum_path_count2(root,targetSum):
    count = [0]
    sum_paths = {0:1}

    def sum_path_3(root,acc_sum):
        if not root:
            return None

        acc_sum += root.data
        diff = acc_sum - targetSum
        if diff in sum_paths:
            count[0] += sum_paths[diff]
        
        if acc_sum in sum_paths:
            sum_paths[acc_sum] += 1
        else:
            sum_paths[acc_sum] = 1


        sum_path_3(root.left,acc_sum)
        sum_path_3(root.right,acc_sum)

        sum_paths[acc_sum] -= 1


    sum_path_3(root,0)
    return count[0]


print(targetsum_path_count1(root,145))
print(targetsum_path_count2(root,145))