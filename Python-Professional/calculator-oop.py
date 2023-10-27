

class Calculator:
    def getInput(self):
        print("We are taking input")
        
    def __init__(self,name:str,age:int):
        self.getInput()


cal = Calculator("Talha",23)

print(cal.name)
print(cal.age)

cal.getInput()