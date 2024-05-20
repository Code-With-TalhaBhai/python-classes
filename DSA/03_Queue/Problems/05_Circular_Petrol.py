
# lis[][0]:Petrol
# lis[][1]:Distance


# lis = [[4,6],[6,5],[7,3],[4,5]] 
lis = [[55,52],[33,100],[77,61],[40,69]]



#brute force(O n^2)
def tour1():
    balance = 0

    for num in range(len(lis)):
        balance += lis[num][0]
        front = num - 1
        rear =  (num) % len(lis)

        while front <= rear:
            if front == rear:
                return front + 1
            
            if front == -1:
                front = 0

            if balance < lis[rear][1]:
                balance = 0
                break

            
            rear = (rear + 1) % len(lis) # circular behaviour           
            balance += lis[rear][0]
    return -1



def tour2():
        balance = 0
        deficit = 0
        point = 0

        for index,item in enumerate(lis):
            petrol = item[0]
            distance = item[1]

            balance += petrol - distance

            if balance < 0:
                deficit += balance
                point = index + 1
                balance = 0


        if deficit + balance >= 0:
            return point
        else:
            return -1


    


print(tour1())
print(tour2())