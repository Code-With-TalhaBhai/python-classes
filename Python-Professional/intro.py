
num1 = int(input("Enter number 1: "));
num2 = int(input("Enter number 2: "));

print(f"The sum is: {num1+num2}");


# Conditionals
if(num1>num2):
    print("num1 is greater than num2");
elif(num2>num1):
    print("num2 is greater than num1");
else:
    print("num1 and num2 are equal");



# loops

print("first loop")
for s in [0,1,2]:
    print(s);


print("second loop")
for s in [3,452,5]:
    print(s);


print("Third loop")
for i in range(2,5):  # similar to for loop in other languages
    print(i);


print("Forth Loop")
for i in range(0,11,2): # 0 to 10, but with increment of 2
    print(i);