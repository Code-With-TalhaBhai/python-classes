

from os import close


def generate_paranthesis(n):
    res = []



    def backtrack(open_brc,close_brc,ans_brc):
        if open_brc == n and close_brc == n:
            # res.append("".join(ans_brc)) # with array
            res.append(ans_brc)
            return
        
        if open_brc < n:
            # ans_brc.append("(") # with list
            ans_brc += "(" # with string
            backtrack(open_brc+1,close_brc,ans_brc)
            # ans_brc.pop() # with list
            ans_brc = ans_brc[:-1] # with string


        if close_brc < open_brc:
            # ans_brc.append(")") # with list
            ans_brc += ")" # with string
            backtrack(open_brc,close_brc+1,ans_brc)  
            # ans_brc.pop() # with list

        
    backtrack(0,0,"")
    # backtrack(0,0,[])
    return res



print(generate_paranthesis(3))
print(generate_paranthesis(2))