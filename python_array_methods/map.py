

arr : list[int] = [1,2,3,4,5,6,7,8,9,10]
def func(element:int)->int:
    return element*2

# double_arr = map(func,arr)
double_arr : list[int] = list(map(func,arr))
square_arr : list[int] = list(map(lambda element: element**2,arr))
print(double_arr)
print(square_arr)