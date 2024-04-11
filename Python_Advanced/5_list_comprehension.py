
names = ["talha","khizer","abrar"]

# For All values 
print("For all values")
uppercased = [str.title(name) for name in names]
print(uppercased)


# For Filtered values
print()
print("for filtered values")
students = [
    {"name": "Talha", "city":"Lahore"},
    {"name": "Jazib", "city":"Lahore"},
    {"name": "Aryaan", "city":"Sialkot"},
    {"name": "Hassan", "city":"Lahore"},
    {"name": "Umer", "city":"Faislabad"},
]

lhr_students = [std["name"] for std in students if std["city"]=="Lahore"]
print(lhr_students)


print()
print("for filtered values else included")
all_students = [std["name"] if std["city"]=="Lahore" else "Not From Lhr" for std in students]
print(all_students)
