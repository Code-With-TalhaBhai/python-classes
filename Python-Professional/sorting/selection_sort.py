


arr = [9,8,0,7,5,6,4,2,3,1];
print(arr)


def selection_sort(arr):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                #swap technique in python
                arr[i],arr[j] = arr[j],arr[i]




selection_sort(arr);
print(arr);