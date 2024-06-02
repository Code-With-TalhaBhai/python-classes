from binarytree import root

# Hint: arr.append(num) -> Make changes to existing arr
# arr = arr + [4] -> Return new arr


def sum_path_2(root,targetSum):
    output = []
    def path_sum_2(root,sum,path):
        if not root:
            return 
        sum += root.data;
        newPath = path + [root.data];

        left = path_sum_2(root.left,sum,newPath);
        right = path_sum_2(root.right,sum,newPath);
    
        if not root.left and not root.right and sum == targetSum:
            output.append(newPath)

    path_sum_2(root,0,[])
    print(output)




sum_path_2(root,145)
sum_path_2(root,85)