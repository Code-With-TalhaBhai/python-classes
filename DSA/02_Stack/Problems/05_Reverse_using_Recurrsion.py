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

    def reverse_stack1(self):
        if not self.__container:
            return

        top = self.peek()
        self.pop()
        # top = self.pop
        self.reverse_stack1()
        self.insertAtBottom(top)


    def reverse_stack2(self,stack:list[str])->list[str]:
        if not self.__container:
            return stack
        
        top = self.pop()
        stack.append(top)
        self.reverse_stack2(stack) 
        self.append(top)
        return stack
                


s = Stack()

s.append(0)
s.append(1)
s.append(2)
s.append(3)
s.append(4)

s.print_stack()

# Method 1 -> without external stack
# s.reverse_stack1()
# s.print_stack()

# Method 2 -> with external stack
print(s.reverse_stack2([]))
