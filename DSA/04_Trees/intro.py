

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


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(100)
root.insert(50)
root.insert(25)
root.insert(150)
root.insert(75)
root.insert(200)
root.printTree()