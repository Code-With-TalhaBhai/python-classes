


class Node:
    def __init__(self,key,data=0) -> None:
        # self.head : Node | None = None
        # self.tail : Node | None = None
        self.head : Node | None = None
        self.tail : Node | None = None
        self.key = key
        self.value = data



class LRUCache:

    def __init__(self, capacity: int):
        self.MRU = None
        self.LRU = None
        # self.MRU : Node = Node()
        # self.LRU : Node = Node()
        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:
        if key in self.cache:
            Node_To_Get = self.cache[key]
            # new
            if Node_To_Get != self.MRU:
                temp = Node_To_Get.head
                # node -> LRU
                if Node_To_Get == self.LRU:
                    self.LRU = temp
                # node -> LRU.head
                if Node_To_Get == self.LRU.head:
                    self.LRU.head = temp
                temp.tail = Node_To_Get.tail
                Node_To_Get.head = None
                Node_To_Get.tail = self.MRU
                self.MRU.head = Node_To_Get
                self.MRU = Node_To_Get
            else:
                print('it is mru')
            # old
            # if Node_To_Get != self.MRU:
            #     temp = Node_To_Get.head
            #     # 1st case
            #     if Node_To_Get == self.LRU:
            #         if temp == self.MRU:
            #             self.LRU.head = self.MRU
            #         self.LRU = temp
            #     # elif Node_To_Get == self.LRU.head:
            #     #     self.LRU.head = temp
            #     temp.tail = Node_To_Get.tail
            #     temp = None
            #     Node_To_Get.tail = self.MRU
            #     self.MRU = Node_To_Get
            # print(self.MRU.value, self.LRU.value)
            return self.MRU.value
        else:
            return -1
        

    def make_node(self,key,value):
        newNode = Node(key,value)
        if self.MRU == None and self.LRU == None:
            self.LRU = newNode
            self.MRU = newNode
        else:
            newNode.tail = self.MRU
            # temp_node = self.cache[self.LRU.key]
            # temp_node.head = newNode
            self.MRU.head = newNode
            self.MRU = newNode
        self.cache[key] = newNode




    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            Node_To_Get = self.cache[key]
            Node_To_Get.key = key
            Node_To_Get.value = value
            self.get(key)
        else:
            if len(self.cache) == self.capacity: #Adding New Node
                temp = self.LRU  
                if self.capacity == 1:
                    self.MRU = None
                    self.LRU = None
                else:
                    self.LRU = temp.head
                    temp.head.tail = None 
                self.cache.pop(temp.key)
                temp = None
            self.make_node(key,value)
            # print(self.MRU.value, self.LRU.value)



# lRUCache = LRUCache(2)
# lRUCache.put(1, 1) 
# lRUCache.get(1)
# print(lRUCache.MRU.value, lRUCache.LRU.value)
# lRUCache.put(2, 2) 
# lRUCache.get(2) 
# print(lRUCache.MRU.value, lRUCache.LRU.value)
# print(lRUCache.get(1))   
# print(lRUCache.MRU.value, lRUCache.LRU.value)
# lRUCache.put(3, 3)
# print(lRUCache.MRU.value, lRUCache.LRU.value)


lRUCache = LRUCache(3)
nums = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
for i in range(1,len(nums)):    
    if len(nums[i]) == 2:
        lRUCache.put(nums[i][0],nums[i][1])
    else:
        print('get',lRUCache.get(nums[i][0]))
    print(lRUCache.MRU.value, lRUCache.LRU.value)
    

# print(lRUCache.get(2))   
# lRUCache.put(4, 4)
# print(lRUCache.get(1))   
# print(lRUCache.get(3))   
# print(lRUCache.get(4))
# print(lRUCache.get(2))


                   


        
        