
students = ["Talha","Qamber","Hassan"]


lhr_students = [{"name":st,"city":"Lahore"} for st in students] # list comprehension
print(lhr_students)

print()
lhr_students1 = {st:"Lahore" for st in students} # dictionary comprehension
print(lhr_students1)