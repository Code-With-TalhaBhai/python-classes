
def check_paranthesis(paranthesis)->bool:
    stack = []
    for _ in range(len(paranthesis)):
        ch = paranthesis[_]

        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)
        else:
            # print('working else')
            open_brc = stack[-1]
            if open_brc == "(" and ch == ")" or open_brc == "{" and ch == "}" or open_brc == "[" and ch == "]":
                stack.pop()

    if not stack:
        return True
    

    return False


def check(output)->None:
    if output == True:
        print("Valid Paranthesis")
    else:
        print("Invalid")




str1 :str = "[()]{}{[()()]()}";
str2 :str = "[[{}[]]]";
str3 :str = "[{{}(]]";
str4 :str = "[](){}";


check(check_paranthesis(str1))
check(check_paranthesis(str2))
check(check_paranthesis(str3))
check(check_paranthesis(str4))