

def generateParenthesis(n: int):
    output = []

    def generate_braces(l,r,bracket):
        if l == n and r == n:
            output.append(bracket)
            return 
        
        if l < n:
            bracket += "("
            generate_braces(l+1,r,bracket)
            bracket = bracket[:-1]
        
        if r < l:
            bracket += ")"
            generate_braces(l,r+1,bracket)


    generate_braces(0,0,"")
    return output



print(generateParenthesis(3))