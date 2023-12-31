
# __call__,__repr__,__str__ remaining

# str and repr remaining

# class MyClass:

#     def __init__(self) -> None:
#         print('Constructor working')

#     def custom(self):
#         return 'custom working'
    
# myclass = MyClass()

# print(myclass.__str__())

class SpecialMethodsExample:
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return f"SpecialMethodsExample with value {self.value}"
    
    def __repr__(self) -> str:
        return f"SpecialMethodsExample({self.value})"
    
    def __call__(self, *args, **kwargs):
        return f"Called with args: {args} and kwargs: {kwargs}"
    


sme = SpecialMethodsExample('234')
print(sme)
print(sme())
print(sme.__repr__())