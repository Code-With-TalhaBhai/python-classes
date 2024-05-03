from collections import deque


class Stack:
    def __init__(self):
        self.__container = []

    def append(self,data):
        self.__container.append(data)

    def pop(self):
        return self.__container.pop()

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
            self.append(data)
            return

        top = self.pop()
        self.insertAtBottom(data)
        self.append(top)

    def sort_stack(self):
        # if len(self.__container)<=1:
        #     return
        if not self.__container:
            return
        
        value = self.__container.pop()
        self.sort_stack()
        if(self.__container and value < self.__container[0]):
            self.insertAtBottom(value)
        else:
            self.append(value)
        print(self.__container)
    
                


s = Stack()

s.append(2)
s.append(0)
s.append(4)
s.insertAtBottom(23)
s.append(1)
s.append(3)

s.print_stack()
s.sort_stack()
s.print_stack()

