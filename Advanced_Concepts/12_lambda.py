# In Python, a lambda function is a small anonymous function defined using the lambda keyword. It can have any number of arguments, but only one expression.


# lambda arguments: expression

add = lambda x,y: x+y
print(add(23,6534))


numbers = [1, 2, 3, 4, 5, 6]
def even_func(x):
    return x%2 == 0

even_number1 = list(filter(even_func, numbers)) # outside function
even_number2 = list(filter(lambda x:x%2==0,numbers)) # lambda function
# Without lambda
print(even_number1)
print("With lambda")
print(even_number2)



double_number = list(map(lambda x:x*2,numbers))
print(double_number)