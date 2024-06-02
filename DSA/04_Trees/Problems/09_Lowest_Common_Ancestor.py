from binarytree import root



def lower_common_ancestor(n1,n2,root):
    curr = root

    while curr:
        if n1 < curr.data and n2 < curr.data:
            curr = curr.left
        elif n1 > curr.data and n2 > curr.data:
            curr = curr.right
        else:
            return curr.data




print(lower_common_ancestor(10,30,root))
print(lower_common_ancestor(25,70,root))
print(lower_common_ancestor(30,40,root))