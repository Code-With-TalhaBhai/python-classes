# Heap is a complete binary tree which start filling from left towards right, in which all levels are filled, except possibly the last one.


# Max Heap - In which parent node is greater than child node
# Min Heap - In which child node is greater than parent node


class Heap():

    def __init__(self):
        self.size = 100
        self.heap_arr : list[None|int] = [None for i in range(self.size)]
        self.top = 0

        self.heap_arr[self.top] = -1
        self.top += 1 



    def insert(self,val):
        self.heap_arr[self.top] = val
        current_idx = self.top

        while current_idx > 1:
            parent_idx = self.top // 2
            if self.heap_arr[current_idx] > self.heap_arr[parent_idx]: # type: ignore
                self.heap_arr[current_idx],self.heap_arr[parent_idx] = self.heap_arr[parent_idx],self.heap_arr[current_idx] # Swapping Values
                current_idx = parent_idx
            else:
                break

        self.top += 1

    
    def deletion(self,val):
        ...
    

    def heapify(self,arr):
        for item in arr:
            self.insert(item)

    def print(self):
        for i in range(1,self.top):
            print(self.heap_arr[i],end=" ")
        print()



heap = Heap()
# Inserting elements through arr is known as heapify
arr = [50,55,53,52,54]
heap.heapify(arr)
heap.print()


