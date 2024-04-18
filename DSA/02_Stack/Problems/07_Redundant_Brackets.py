
def redundant_bracket(str)->bool:
    stack = []
    for _ in range(len(str)):
        ch = str[_]

        if ch == "(" or ch == "+" or ch == "-" or ch == "*" or ch == "/":
            stack.append(ch)

        if ch == ")":
            top = stack[-1]
            if top == "+" or top =="-" or ch == "*" or ch == "/":
                top_pop = stack.pop()
                while top_pop != "(":
                    top_pop = stack.pop()

        if not stack:
            return False
            

    return True




def check(output)->None:
    if output == True:
        print("Redundant")
    else:
        print("Not Redundant")




str1:str = "(a+c*b)+(c))";
str2:str = "(a+b)";
str3:str = "((a+b))";


check(redundant_bracket(str1))
check(redundant_bracket(str2))
check(redundant_bracket(str3))
