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



s = Stack()

s.append(1)
s.append(2)
s.append(3)
print(s.peek())
s.pop()
print(s.peek())
