

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


    def InOrderTraversal(self,root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res
    

    def PreOrderTraversal(self,root):   
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res


    def PostOrderTraversal(self,root):
        res = []
        if root:
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res


    



def InOrder(root):

        res = []
        if root:
            res = InOrder(root.left)
            res.append(root.data)
            res = res + InOrder(root.right)

        return res



root = Node(50)
root.insert(25)
root.insert(10)
root.insert(70)
root.insert(60)
root.insert(30)
root.insert(40)


print(root.InOrderTraversal(root)) # LNR(Left-Node-Right)
print(root.PreOrderTraversal(root)) # NLR(Node-Left-Right)
print(root.PostOrderTraversal(root)) # LRN(Left-Right-Node)



print(InOrder(root)) # Outside class