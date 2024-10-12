

def isSubsetSum(arr, target_sum):
    
    def subsets(i,sum):
        if i >= len(arr):
            if sum == target_sum:
                return True
            return False
        
        if subsets(i+1,sum) or subsets(i+1,sum+arr[i]):
            return True


    return subsets(0,0)


arr = [3, 34, 4, 12, 5, 2]
print(isSubsetSum(arr,9))