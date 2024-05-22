  

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data



# def simple_insertion(root,val):

#     if root == None:
#         root = Node(val)
#         return root
#     else:
#         if val < root.data:
#             if root.left == None:
#                 root.left = Node(val)
#             else:
#                 root.left = simple_insertion(root.left,val)
#         elif val > root.data:
#             if root.right == None:
#                 root.right = Node(val)
#             else:
#                 root.right = simple_insertion(root.right,val)
#         return root


def simple_insertion(root,val):

    if root == None:
        root = Node(val)
        return root
    else:
        if val < root.data:
            root.left = simple_insertion(root.left,val)
        elif val > root.data:
            root.right = simple_insertion(root.right,val)
        return root


def InOrderTraversal(root):
        res = []
        if root:
            res = InOrderTraversal(root.left)
            res.append(root.data)
            res = res + InOrderTraversal(root.right)
        return res




level_order = [50,25,10,70,60,30,40]

def construct_tree():
    root = simple_insertion(None,level_order[0])
    for i  in range(1,len(level_order)):
        simple_insertion(root,level_order[i])
    return root

# root = Node(50)
# root = simple_insertion(None,53)
# simple_insertion(root,25)
# simple_insertion(root,10)
# simple_insertion(root,70)
# simple_insertion(root,60)
# simple_insertion(root,30)
# simple_insertion(root,40)

# print(InOrderTraversal(root))
print(InOrderTraversal(construct_tree()))
