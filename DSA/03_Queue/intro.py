
# FIFO -> First-In-First-Out
class Queue:
    def __init__(self):
        self.queue = []

    def push(self,data):
        return self.queue.insert(0,data)

    def pop(self):
        return self.queue.pop()

    def peek(self):#front
        return self.queue[-1]

    def empty(self):
        if(len(self.queue)==0):
            return True
        else:
            return False
        
        
