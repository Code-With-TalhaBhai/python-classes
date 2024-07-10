# Heap is a complete binary tree which start filling from left towards right, in which all levels are filled, except possibly the last one.


# Max Heap - In which parent node is greater than child node
# Min Heap - In which child node is greater than parent node


class Heap():

    def __init__(self):
        self.size = 100
        self.heap_arr : list[int] = [-1 for i in range(self.size)]
        self.top = 0

        self.heap_arr[self.top] = -1
        self.top += 1 



    def insert(self,val):
        self.heap_arr[self.top] = val
        current_idx = self.top

        while current_idx > 1:
            parent_idx = current_idx // 2
            if self.heap_arr[current_idx] > self.heap_arr[parent_idx]:
                self.heap_arr[current_idx],self.heap_arr[parent_idx] = self.heap_arr[parent_idx],self.heap_arr[current_idx] # Swapping Values
                current_idx = parent_idx
            else:
                break

        self.top += 1

    
    # def deletion(self,val):
        
    #     for index,item in enumerate(self.heap_arr):
    #         if val == self.heap_arr[index]:
    #             break

    #     self.heap_arr[index],self.heap_arr[self.top-1] = self.heap_arr[self.top-1],self.heap_arr[index]
    #     self.heap_arr.pop(self.top-1)

    #     left_child = 2 * index
    #     right_child = (2 * index) + 1

    #     self.top -= 1

    #     if left_child < self.top and right_child < self.top:
    #         if self.heap_arr[left_child] > self.heap_arr[right_child] and self.heap_arr[left_child] > self.heap_arr[index]: # type: ignore
    #             self.heap_arr[left_child],self.heap_arr[index] = self.heap_arr[index],self.heap_arr[left_child]
            

    def pop(self):
        if self.top < 2:
            return

        self.top -= 1
        self.heap_arr[1],self.heap_arr[self.top] = self.heap_arr[self.top],self.heap_arr[1]
        self.heap_arr.pop() 


        root_index = 1
        while root_index < self.top:
            leftChild = 2 * root_index
            rightChild = 2 * root_index + 1
            largest = root_index

            if largest <= leftChild and self.heap_arr[largest] < self.heap_arr[leftChild]:
                largest = leftChild
            if largest <= rightChild and self.heap_arr[largest] < self.heap_arr[rightChild]:
                largest = rightChild


            if largest != root_index:
                self.heap_arr[largest],self.heap_arr[root_index] = self.heap_arr[root_index],self.heap_arr[largest]
            else:
                return

            root_index = largest


            



        



        
        

    def print(self):
        for i in range(1,self.top):
            print(self.heap_arr[i],end=" ")
        print()



heap = Heap()
# Inserting elements through arr is known as heapify
# arr = [50,55,53,52,54]
arr = [46,32,34,33,43,22,50,44]
for item in arr:
    heap.insert(item)

heap.pop()
# heap.pop()
heap.print()


