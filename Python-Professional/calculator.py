
a : int = int(input("Enter first input: "));
b : int = int(input("Enter second element: "));


operation = input("Enter which operation you want to perform: ");


if(operation == "+"):
    print(f"The addition of {a} + {b} = {a+b}")
elif(operation == "-"):
    print(f"The addition of {a} - {b} = {a-b}")
elif(operation == "*"):
    print(f"The addition of {a} * {b} = {a*b}")
elif(operation == "/"):
    print(f"The addition of {a} / {b} = {a/b}")
else:
    print("Enter the correct operator")