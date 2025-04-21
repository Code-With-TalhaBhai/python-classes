

class SegmentTree():

    def __init__(self,arr) -> None:
        self.arr = arr
        self.n = len(arr)
        self.segmentTree = [-1] * (self.n * 2)
        # print(self.segmentTree)


def buildTree(l,r,root,i):
    if l == r:
        root.segmentTree[i] = root.arr[l]
        return 

    mid = (l + r) // 2
    buildTree(l,mid,root,2*i+1)
    buildTree(mid+1,r,root,2*i+2)

    root.segmentTree[i] = root.segmentTree[2*i+1] + root.segmentTree[2*i+2]


def query(low,high,root,l=0,r=0):
    if low == l and high == r:
        return root.segmentTree



arr = [3,1,2,7,1]
root = SegmentTree(arr) # Sum Segment Tree
buildTree(0,(root.n)-1,root,0)
print(root.segmentTree)

query(1,3,root)