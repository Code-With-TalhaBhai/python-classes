from binarytree import root
import collections


# Short but modifies the original tree
def morris_inorder_traversal1(root):
    curr = root

    while curr is not None:
        if curr.left is None:
            print(curr.data,end=" ")
            curr = curr.right
        else:
            predecessor = curr.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            predecessor.right = curr

            temp = curr
            curr = curr.left
            temp.left = None
    print()


# Extra steps, create temporary links(threads) but modifies to its original state
def morris_inorder_traversal2(root):
    if not root:
        return None
    
    curr = root

    while curr:
        if not curr.left:
            print(curr.data,end=" ")
            curr = curr.right
        else:
            # print('curr: ',curr.data)
            predecessor = curr.left
            # print('pres ',predecessor.data)
            while predecessor.right is not None and predecessor.right != curr:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                predecessor.right = curr
                curr = curr.left
            elif predecessor.right == curr:
                print(curr.data,end=" ")
                curr = curr.right
                predecessor.right = None

    print()





def Level_Order_Traversal(root):
        dq = collections.deque()
        if root:
            dq.append(root)
        res = []

        while dq:
            level_nodes = []
            qlen = len(dq)

            for i in range(qlen):
                root = dq.popleft()     
                left = root.left
                right = root.right

                if left is not None:
                    dq.append(left)
                if right is not None:
                    dq.append(right)

                level_nodes.append(root.data)
            res.append(level_nodes)
        return res




# morris_inorder_traversal1(root)
# print(Level_Order_Traversal(root))# for checking


morris_inorder_traversal2(root)
print(Level_Order_Traversal(root))# for checking

