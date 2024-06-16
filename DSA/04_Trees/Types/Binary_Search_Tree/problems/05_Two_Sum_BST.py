from bst import root


def findTarget(root,k):
    traversed_values = {}
    def twoSum(root):
        if not root:
            return False

        if k-root.data in traversed_values:
            return True
        else:
            traversed_values[root.data] = True

        return twoSum(root.left) or twoSum(root.right)

    return twoSum(root)


print(findTarget(root,50))