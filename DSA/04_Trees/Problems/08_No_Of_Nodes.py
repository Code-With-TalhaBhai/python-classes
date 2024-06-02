from binarytree import root


def count_nodes1(root):
    num = [0]

    def nodes(root):
        if not root:
            return 
        
        left = nodes(root.left)
        right = nodes(root.right) 

        num[0] = num[0] + 1

    nodes(root)
    return num[0]


print(count_nodes1(root))
