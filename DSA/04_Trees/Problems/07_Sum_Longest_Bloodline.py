from binarytree import root


def SumOfLongestBloodLine(root):
    paths_sum = {}
    def longest_bloodline(root,no_of_nodes,sum):
        if not root:
            if no_of_nodes in paths_sum:
                sum = max(paths_sum[no_of_nodes],sum)
            paths_sum[no_of_nodes] = sum
            return

        no_of_nodes += 1
        sum += root.data
    
        longest_bloodline(root.left,no_of_nodes,sum)
        longest_bloodline(root.right,no_of_nodes,sum)

    longest_bloodline(root,0,0)
    maxi = max(paths_sum)
    return paths_sum[maxi]


print(SumOfLongestBloodLine(root))