
names = ["talha","khizer","abrar"]


def func(name):
    # return "\n"+str.title(name) + " Developer"
    return str.title(name) + " Developer"

new_list = map(func,names)

print(list)
print(*new_list)


new_list1 = list(map(func,names))
print(new_list1)