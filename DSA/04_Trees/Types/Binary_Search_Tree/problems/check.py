# mergeing sorted bsts

arr1 = [1,3,4]
arr2 = [2,6,7,8,9]
arr3 = []
i = j = 0

len1 = len(arr1)
len2 = len(arr2)


while i < len1  and j < len2:
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    elif arr1[i] > arr2[j]:
        arr3.append(arr2[j])
        j += 1


while i < len1:
    arr3.append(arr1[i])
    i+=1

   
while j < len2:
    arr3.append(arr2[j])
    j += 1