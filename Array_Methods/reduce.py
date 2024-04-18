import functools
arr : list[int] = [1,2,3,4,5,6,7,8,9,10]
def func(total,curr):
    return total + curr

arr_sum : int = functools.reduce(func,arr)
arr_mul : int = functools.reduce(lambda total,curr : total*curr,arr)
print(arr_sum)
print(arr_mul)