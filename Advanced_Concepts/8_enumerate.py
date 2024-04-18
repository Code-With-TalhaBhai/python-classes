# enumerate is a built-in function in python, that allows
# you to keep track of the number of iterations (loops) in a loop


students = ["Talha","Qamber","Hassan"]

# enumerate(iterable,start)

for i in enumerate(students,start=1):
    print(i)

# enumerate returns (index,value) both
for i,student in enumerate(students,start=1):
    print(i,". "+student)