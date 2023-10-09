i = 1

print("first loop")
while i <= 5:
    print(i)
    i += 1;


print("second loop")
i = 3;
while i <= 15:
    print(i)
    i += 3;


print("Third loop-->Continue")
i = 0;
while i<10:
    i+=2;
    if i == 6:
        continue

    print(i);


print("Forth loop --> Break")
i = 0;

while i<10:
    if i == 6:
        break

    i+=2
    print(i)