
        

def lemonadeChange(bills) -> bool:
    
    fives = 0
    tens = 0
    n = len(bills)

    for i in range(n):
        customer_pay = bills[i]

        if customer_pay == 10:
            tens += 1
            if fives > 0:
                fives -= 1
            else:
                return False
        
        elif customer_pay == 20:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False

        else:
            fives += 1

    return True




bills1 = [5,5,5,10,20]
bills2 = [5,5,10,10,20]
print(lemonadeChange(bills1))
print(lemonadeChange(bills2))