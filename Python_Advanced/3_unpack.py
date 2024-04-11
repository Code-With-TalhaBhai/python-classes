full_name = "talha,bhai,young"

first,last,status = full_name.split(",")
print(first)
print(last)
print(status)
print()

def findPower(force:int,displacement:int,time:int):
    power = (force*displacement)/time
    print(power)
    return power

print("Simple")
findPower(435,64,4)
print("List Unpacking")
variables = [435,64,4]
findPower(*variables) #Unpacking


var_dict = {
    "force": 435,
    "time": 4,
    "displacement": 64,
}

# findPower(var_dict["force"],var_dict["displacement"],var_dict["time"])
print("Dictionary Unpacking")
findPower(**var_dict)
print()

# *args vs **kwargs
# *args: Number of Positional Arguements
# **kwargs: Number of keyword arguments
def func(*args,**kwargs):
    print("Positional_Arguments: ",type(args),args)
    print("keyword_arguments: ",type(kwargs),kwargs)


print("Only positional arguments")
func(23,52,35,64)
print("Only keyword arguments")
func(force=23,power=52,distance=35,time=64)
print()

