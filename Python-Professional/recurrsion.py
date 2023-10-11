

# Factorial

n = int(input("Enter the value: "))
def factorial(n):
    if(n==1):
        return 1;
    
    return n * factorial(n-1);


print(f"The factorial of {n} is: {factorial(n)}")