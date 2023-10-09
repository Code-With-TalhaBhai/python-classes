
num1 = int(input("Enter number 1: "));
num2 = int(input("Enter number 2: "));


# Conditionals
if(num1>num2):
    print("num1 is greater than num2");
elif(num2>num1):
    print("num2 is greater than num1");
else:
    print("num1 and num2 are equal");




mystr = input("Enter any string: ");


if(mystr.lower() in ['y','yes']):
    print("Yes is typed")
elif(mystr.lower() in ['n','no']):
    print("No is typed")
else:
    print("some other thing is typed")