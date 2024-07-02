

class HashMap():
    
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]


    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX
    

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

my_dict = HashMap()

# print(my_dict.get_hash('age'))
# print(my_dict.get_hash('23'))

my_dict['name'] = 'Talha'
my_dict['age'] = 21
my_dict['profession'] = 'Developer'
my_dict['age'] = 232
# my_dict['23'] = 'Millionaire' # Collision occurs with `name`


print(my_dict['profession'])
print(my_dict['name'])
print(my_dict['age'])
# print(my_dict['23'])

del my_dict['age']
print()

print(my_dict['profession'])
print(my_dict['name'])
print(my_dict['age'])
# print(my_dict['23'])

# print()
# print(my_dict.arr)
