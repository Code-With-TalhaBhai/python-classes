
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)


# In Progress
def height_using_node(root):
    if root is None:
        return 0
    
    left = height_using_node(root.left)
    right = height_using_node(root.right)

    height = max(left,right) + 1
    return height


def height_using_edges(root):
    if root == None:
        return -1

    left = height_using_edges(root.left)
    right = height_using_edges(root.right)

    height = 1 + max(left,right)
    return height



root = Node(50)
root.insert(25)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(40)


print("Height using Nodes: ",height_using_node(root))
print("Height using Edges: ",height_using_edges(root))