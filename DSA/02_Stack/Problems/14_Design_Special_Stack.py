
class Stack:
    stack = []
    min = -1

    def push(self,data):
        if not self.stack:
            self.min = data
            self.stack.append(data)
            return 

        if(data<self.min):
            updated_data = data - self.min
            self.min = data
            self.stack.append(updated_data)
        else:
            self.stack.append(data)
        

    def pop(self):
        if not self.stack:
            return -1
        
        value = self.stack.pop()
        if value < self.min:    
            prevMin = self.min
            self.min = prevMin - value


    def top(self):
        if self.stack[-1] < self.min:
            return self.min
        return self.stack[-1]

    def mini(self):
        return self.min
    
    def print_stack(self):
        for items in self.stack:
            print(items,end=" ")
        print()


stack = Stack()
stack.push(5)
stack.push(15)
stack.push(2)
stack.push(4)
stack.push(1)
stack.push(65)

print("Stack top is: ",stack.top())
print("Stack mini is: ",stack.mini())
print()
print("After Pop")
print()
stack.pop()
stack.pop()


# stack.print_stack()
print("Stack top is: ",stack.top())
print("Stack mini is: ",stack.mini())
