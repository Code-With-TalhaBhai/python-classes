

students = [
    {"name": "Talha", "city":"Lahore"},
    {"name": "Jazib", "city":"Lahore"},
    {"name": "Aryaan", "city":"Sialkot"},
    {"name": "Hassan", "city":"Lahore"},
    {"name": "Umer", "city":"Faislabad"},
]


def st_filter(student):
    if(student['city']=='Lahore'):
        return True
    else:
        return False
    

filtered_students = filter(st_filter,students)


# print(list(filtered_students))# As, its a filter object
# print(*filtered_students)# As, its a filter object

for st in filtered_students:
    print(st)