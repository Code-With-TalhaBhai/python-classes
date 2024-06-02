from binarytree import root

# 110

def path_sum_1(root,targetSum):

    def path_sum(root,sum):
        if not root:
            return False

        sum += root.data

        if not root.left and not root.right and sum == targetSum:
            return True
        
        return path_sum(root.left,sum) or path_sum(root.right,sum)
        # left = path_sum(root.left,sum)
        # right = path_sum(root.right,sum)
        # return left or right

    return path_sum(root,0)
    


print("The targetSum is 180",path_sum_1(root,180))
print("The targetSum is 85",path_sum_1(root,85))
print("The targetSum is 145",path_sum_1(root,145))
print("The targetSum is 110",path_sum_1(root,110))