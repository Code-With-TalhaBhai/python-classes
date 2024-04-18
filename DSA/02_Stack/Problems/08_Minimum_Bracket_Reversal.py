

def minimum_bracket_reversal(brackets:str)->int:
    if(len(brackets)%2==1):
        return -1
    
    stack = []

    for _ in range(len(brackets)):
        ch = brackets[_]
        # top = stack[-1]
        if stack and stack[-1] == "{" and ch == "}":
            stack.pop()
        else:
            # top = ch
            stack.append(ch)

    open_brc = 0
    close_brc = 0

    while stack:
        top = stack[-1]
        if top == "{":
            open_brc = open_brc + 1
        elif top == "}":
            close_brc = close_brc + 1
        stack.pop()

    # print(open_brc)
    # print(close_brc)
    count = int((open_brc+1)/2) + int((close_brc+1)/2)
    return count



str1 : str = "{{{}";
str2 : str = "{{}{}}";
str3 : str = "{{{{";
str4 : str = "{}}{}}";



print("The minimum cost of bracket reversal is: ",minimum_bracket_reversal(str1))
print("The minimum cost of bracket reversal is: ",minimum_bracket_reversal(str2))
print("The minimum cost of bracket reversal is: ",minimum_bracket_reversal(str3))
print("The minimum cost of bracket reversal is: ",minimum_bracket_reversal(str4))