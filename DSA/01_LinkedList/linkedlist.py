
def print_list(node):
    curr_node = node
    while curr_node is not None:
        print(curr_node.data)
        curr_node = curr_node.nextNode



class Node:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode



n1 = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")


n1.nextNode = n2
n2.nextNode = n3

print_list(n1)

