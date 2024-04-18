from collections import deque


class Stack:
    def __init__(self):
        self.__container = []

    def append(self,data):
        self.__container.append(data)

    def pop(self):
        self.__container.pop()

    def peek(self):
        return self.__container[-1]
    
    def is_empty(self):
        return len(self.__container) == 0
    
    def size(self):
        return len(self.__container)
    
    def print_stack(self):
        print(self.__container)

    def insertAtBottom(self,data):
        if not self.__container:
            self.__container.append(data)
            return

        top = self.__container.pop()
        self.insertAtBottom(data)
        self.__container.append(top)



s = Stack()

s.append(2)
s.append(3)
s.append(4)
# print("stack top is: ",s.peek)
s.print_stack()
s.insertAtBottom(1)
s.print_stack()
s.insertAtBottom(0)
s.print_stack()



