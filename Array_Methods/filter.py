

arr : list[int] = [1,2,3,4,5,6,7,8,9,10]
def func(element):
   # return element%2==0
   if(element%2==0):
      return element 
   else:
      return False

filtered_arr : list[int] = list(filter(func,arr))
filtered_arr1 : list[int] = list(filter(lambda element : element%2==0,arr))
print(filtered_arr)
print(filtered_arr1)

print('Natural Number Filter')
filtered_natural : list[int] = list(filter(lambda data : data%2==0,range(0,201)))
print(filtered_natural)