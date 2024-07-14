class MedianFinder1:

    def __init__(self):
        self.arr = []


    def insertion_sort(self): # partial-insertion-sort
            i = len(self.arr)-1
            temp = self.arr[i]
            j = i - 1

            while j >= 0 and self.arr[j] > temp:
                self.arr[j+1] = self.arr[j]
                j -= 1

            self.arr[j+1] = temp


    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.insertion_sort()


    def findMedian(self) -> float:
        num = 0
        arr_len = len(self.arr)
        mid = arr_len//2
        if arr_len % 2 == 0:
            num = (self.arr[mid-1] + self.arr[mid])/2
        else:
            num = self.arr[mid]

        return float(num)
             
            

import heapq
class MedianFinder2:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []


    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap,-num)
        else:
            if num < abs(self.maxHeap[0]) :
                heapq.heappush(self.maxHeap,-num)
                if len(self.maxHeap) - len(self.minHeap) > 1:
                    temp = heapq.heappop(self.maxHeap)
                    heapq.heappush(self.minHeap,-temp)

            else:
                heapq.heappush(self.minHeap,num)
                if len(self.minHeap) - len(self.maxHeap) > 1:
                    temp = heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap,-temp)


    def findMedian(self) -> float:
        max_len = len(self.maxHeap)
        min_len = len(self.minHeap)

        num = 0
        if max_len > min_len:
            num = -self.maxHeap[0]
        elif min_len > max_len:
            num = self.minHeap[0]
        elif min_len == max_len:
            num = ((self.minHeap[0]) + (self.maxHeap[0]*-1))/2
        
        return float(num)



# Brute-Force Approach-Time limit exceeded in testcase(leetcode)
obj1 = MedianFinder1()
obj1.addNum(1);    # arr = [1]
obj1.addNum(2);    # arr = [1, 2]
print(obj1.findMedian()); # return 1.5 (i.e., (1 + 2) / 2)
obj1.addNum(3);    # arr[1, 2, 3]
print(obj1.findMedian())


print()
# Optmized Approach - Through Heap
obj2 = MedianFinder2()
obj2.addNum(1);    # arr = [1]
obj2.addNum(2);    # arr = [1, 2]
print(obj2.findMedian()); # return 1.5 (i.e., (1 + 2) / 2)
obj2.addNum(3);    # arr[1, 2, 3]
print(obj2.findMedian())

