# A generator function in Python is defined like a normal function,
# but whenever it needs to generate a value,
# it does so with the yield keyword rather than return.
# If the body of a def contains yield,
# the function automatically becomes a Python generator function. 



def main():
    n = int(input("How many lions you want to print: "))
    for l in lion(n):
       print(l)
   

# it is not printing when n > 1000000 without generator
def lion(n):
    # lions = []
    # for _ in range(n):
        # lions.append("🦁" * _)
    # return lions
    
    #with generator
    for _ in range(n):
        yield "🦁" * _




main()



def my_generator():
    print('start')
    for i in range(5):
        yield i
    print('end')


for generator in my_generator():
    print(generator)



# str = "I am"*3
# print(str)