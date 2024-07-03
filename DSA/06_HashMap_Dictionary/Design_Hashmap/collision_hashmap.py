# In Designing hashmap, `age` and `23` has same hash which results in hash-collision. In order to avoid collision, we use the following solution.This problem can be solve by Separate-Chaining


class HashMap():

    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    
    def gethash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    

    def __setitem__(self,key,value):
        h = self.gethash(key)
        found = False

        if len(self.arr[h]) > 0:
            for idx,item in enumerate(self.arr[h]):
                if item[0] == key:
                    self.arr[h][idx] = (key,value)
                    break


        if not found:
            self.arr[h].append((key,value))


    def __getitem__(self,key):
        h = self.gethash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.gethash(key)

        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return


my_dict = HashMap()
my_dict['name'] = 'Talha'
my_dict['age'] = 21
my_dict['profession'] = 'Developer'
my_dict['23'] = 'Millionaire'
my_dict['age'] = 212

# del my_dict['age']
# del my_dict['23']

print(my_dict['profession'])
print(my_dict['age'])
print(my_dict['name'])
print(my_dict['23'])
