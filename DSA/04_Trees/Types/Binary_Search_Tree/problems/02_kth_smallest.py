from bst import root


def kthSmallest1(root, k: int) -> int:
        res = []
        def k_small(root):
            if not root:
                return None

            k_small(root.left)
            res.append(root.data)
            k_small(root.right)

        k_small(root)
        return res[k-1]



def kthSmallest2(root,k):
    n = 0
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        n += 1
        if n == k:
            return curr.data

        curr = curr.right

            
            






print(kthSmallest1(root,2))
print(kthSmallest2(root,2))