

class Queue:
    def __init__(self,size):
        self.queue = list()
        self.front = self.rear = 0
        self.size = size

    def enqueue(self,data):
        if self.rear >= self.size:
            print("Stack Overflow: Queue is full")
        else:
            self.queue.append(data)
            self.rear = self.rear + 1

    def dequeue(self):
        if self.front == self.rear:
            print("Stack Underflow: Queue is empty")
        else:
            self.queue.pop(0)
            self.rear = self.rear - 1
    
    def print_queue(self):
        if self.front == self.rear:
            print("Stack Underflow: Queue is empty")
        else:
            for item in self.queue: 
                print(item)

    def empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
    def queue_front(self):
        if self.front == self.rear:
            print("Stack Underflow: Queue is empty")  
        else:
            print(self.queue[self.front])

    def queue_rear(self):
        if self.front == self.rear:
            print("Stack Underflow: Queue is empty")
        else:
            print(self.queue[self.rear-1])


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print_queue()
    queue.enqueue(6)
    print("Before popping")
    queue.queue_front()
    queue.queue_rear()


    print("AFter popping")
    queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    queue.queue_front()
    queue.queue_rear()
    # queue.print_queue()
