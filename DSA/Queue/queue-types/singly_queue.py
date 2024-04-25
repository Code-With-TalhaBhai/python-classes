

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Queue:
    def __init__(self) -> None:
        self.front = self.rear = None


    def enqueue(self,data):
        temp = Node(data)
        if self.rear == None:
            self.rear = self.front = temp

        self.rear.next = temp # type:ignore
        self.rear = temp

    def dequeue(self):
        if(self.empty()):
            print("Queue is empty")
            return

        self.front = self.front.next # type:ignore
        if(self.front == None):
            self.rear = None



    def empty(self):
        return self.front == None

    def peek(self):
        if(self.empty()):
            print("Queue is empty")
            return
        print(self.front.data) # type:ignore



# node = Node(34)
# print(node.data)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.peek()
queue.dequeue()

queue.peek()
queue.dequeue()

queue.peek()
queue.dequeue()

queue.peek()
queue.dequeue()

queue.peek()
queue.dequeue()


queue.peek()
