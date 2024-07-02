from collections import defaultdict


# normal_dictionary->Does not return value if not passed
my_dict1 = {}
# default_dictionary->Have default value if retrieved
my_dict2 = defaultdict(int) 
my_dict3 = defaultdict(list) 
my_dict4 = defaultdict(str) 
my_dict5 = defaultdict(lambda: 'default_value_of_function') 
my_dict6 = defaultdict(set) 



# print(my_dict1['name']) # give error
print(my_dict2['names'])
print(my_dict3['names'])
print(my_dict4['names'])
print(my_dict5['names'])
print(my_dict6['names'])