import queue


class Queue:
    def __init__(self,size):
        self.queue = [None for i in range(size)]
        self.front = self.rear = 0
        self.size = size

    # Without Optimization
    # def Enqueue(self,data):
    #     if (self.front == 0 and self.rear == self.size - 1):
    #         print("Queue is full")

    #     elif self.front == -1: # First element to push
    #         self.rear = self.front = 0
    #         self.queue[self.rear]=(data)

    #     elif self.rear == self.size -1 and self.front != 0: # circularly push
    #         self.rear = 0
    #         self.queue[self.rear] = data

    #     else: # Normal push
    #         self.rear = self.rear + 1
    #         self.queue[self.rear] = data

    # With Optimization
    def Enqueue(self,data):
        if (((self.rear + 1)%self.size) == self.front):
            print("Queue is full")
            return False

        elif self.front == -1:
            # print('enting -1')
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            # print('enting')
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

        return True


    def Dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty")
            return -1
        
        ans = self.queue[self.rear]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        
        else:
            self.front = (self.front + 1) % self.size

        return ans

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return 

        elif self.front < self.rear: # Elements are in normal queue format
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()

        else: # elements are in circular queue format
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()

            

        
queue = Queue(7)


queue.Enqueue(46)
queue.Enqueue(6)
queue.Enqueue(4)
queue.Enqueue(446)
queue.Enqueue(643)
queue.Enqueue(64)

queue.Dequeue()
queue.Dequeue()
queue.Dequeue()

queue.Enqueue(1)
queue.Enqueue(2)

queue.display()     