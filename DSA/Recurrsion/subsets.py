


from inspect import findsource


def subsets_str(str):
    result = []

    def find_subset(sub_str,i):
        if i >= len(str):
            result.append(sub_str)
            return sub_str

        find_subset(sub_str,i+1)

        find_subset(sub_str+str[i],i+1)

    find_subset('',0)
    return result


def subsets_list(arr):
    final = []

    def find_subset(ans,i):

        if i >= len(arr):
            # final.append(ans.copy())
            final.append(ans[:])
            return
        
        find_subset(ans,i+1)
        ans.append(arr[i]) # include
        find_subset(ans,i+1)
        ans.pop() # exclude

    find_subset([],0)
    return final


str = "abc"
arr = [1,2,3]
print(subsets_str(str))
print(subsets_list(arr))