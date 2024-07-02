
# Initializing
my_dict1 = {}
my_dict2 = dict()



my_dict1 = {
    'names' : ['talha','aryaan','taha']
}

my_dict1['names'].append('jazib')


# Retrieving values
print(my_dict1.keys())
print(my_dict1.values())
print(my_dict1.items())

print()
print()

# In Python, an iterable is an object capable of returning its members one at a time. Examples of iterables include lists, tuples, strings, dictionaries, sets, and even files. An object is considered iterable if it implements the __iter__() or __getitem__() method.

values_iterator = iter(my_dict1.values())
item_iterator = iter(my_dict1.items())

for value in values_iterator:
    print('value',value)

for item in item_iterator:
    print('item', item)


# print(dir(my_dict1))