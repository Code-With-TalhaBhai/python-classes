


class Node:
    def __init__(self,key,data=0) -> None:
        self.head : Node | None = None
        self.tail : Node | None = None
        self.key = key
        self.val = data



class LRUCache:

    def __init__(self, capacity: int):
        self.MRU = None
        self.LRU = None
        # self.MRU : Node = Node()
        # self.LRU : Node = Node()
        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:
        print(self.cache)
        if key in self.cache:
            Node_To_Get = self.cache[key]
            # 1st way
            if Node_To_Get != self.MRU:
                temp = Node_To_Get.head
                temp.tail = Node_To_Get.tail
                if Node_To_Get == self.LRU:
                    self.LRU = temp
                Node_To_Get.tail = self.MRU
                Node_To_Get.head = None
                self.MRU.head = Node_To_Get
                self.MRU = Node_To_Get
            return self.MRU.val
        else:
            return -1

    def remove(self):
        # if len(self.cache) == self.capacity:
        temp = self.LRU
        self.LRU = temp.head
        self.cache.pop(temp.key)
        if self.LRU is not None:
            self.LRU.tail = None
        temp = None

    def update(self,newNode,key):
        if self.MRU is not None:
            self.MRU.head = newNode
            newNode.tail = self.MRU
            self.MRU = newNode
        else:
            self.MRU = newNode
            self.LRU = newNode
        self.cache[key] = self.MRU


    def put(self, key: int, value: int) -> None:
        # print(self.cache)
        newNode = None
        if key in self.cache:
            newNode = self.cache[key]
            newNode.val = value
            if len(self.cache) -> remove
            self.update(newNode,key)
        else:
            newNode = Node(key,value)
            if self.MRU == None and self.LRU == None:
                self.MRU = newNode
                self.LRU = newNode
                self.cache[key] = newNode
            else:
                if len(self.cache) == self.capacity:
                    self.remove()
                self.update(newNode,key)
        # else:
            # if len(self.cache) == self.capacity:
            #     temp = self.LRU
            #     self.LRU = temp.head
            #     self.cache.pop(temp.key)
            #     if self.LRU is not None:
            #         self.LRU.tail = None
            #     temp = None

            # if self.MRU is not None:
            #     self.MRU.head = newNode
            #     newNode.tail = self.MRU
            #     self.MRU = newNode
            # else:
            #     self.MRU = newNode
            #     self.LRU = newNode
            # self.cache[key] = self.MRU
            # print(self.cache)
        


# lRUCache = LRUCache(2)
# lRUCache.put(1, 1) 
# lRUCache.put(2, 2) 
# print(lRUCache.get(1))   
# lRUCache.put(3, 3)
# print(lRUCache.get(2))   
# lRUCache.put(4, 4)
# print(lRUCache.get(1))   
# print(lRUCache.get(3))   
# print(lRUCache.get(4))
# print(lRUCache.get(2))

# lRUCache.put(1,0)
# lRUCache.put(2,2)
# print(lRUCache.get(1))   
# lRUCache.put(3,3)
# print(lRUCache.get(2))   
# lRUCache.put(4,4)
# print(lRUCache.get(1))   
# print(lRUCache.get(3))   
# print(lRUCache.get(4))   


# lRUCache = LRUCache(2)
# lRUCache.put(1,1)
# lRUCache.put(2,2)
# print(lRUCache.get(1))
# lRUCache.put(3,3)
# print(lRUCache.get(2))
# lRUCache.put(4,4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(4,4))


lRUCache = LRUCache(2)
lRUCache.put(2,1)
lRUCache.put(1,1)
lRUCache.put(2,3)
lRUCache.put(4,1)
print(lRUCache.get(1))
print(lRUCache.get(2))
# lRUCache.put(3,2)
# print(lRUCache.get(3))


# lRUCache = LRUCache(2)
# print(lRUCache.get(2))
# lRUCache.put(2,6)
# print(lRUCache.get(1))
# lRUCache.put(1,5)
# # lRUCache.put(1,2)
# print(lRUCache.get(1))
# print(lRUCache.get(2))


