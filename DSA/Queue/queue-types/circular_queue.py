

class Queue:
    def __init__(self,size):
        self.queue = []
        self.front = self.rare = None
        self.size = size


    def Enqueue(self,data):
        if (self.front == 0 and self.rare == self.size - 1):
            self.queue.append(data)
            self.rare += 1

    def Dequeue(self):
        ...