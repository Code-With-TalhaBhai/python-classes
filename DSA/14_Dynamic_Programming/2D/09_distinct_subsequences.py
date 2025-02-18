


def distinct_subsequences1(s,t):

    def helper(i,j):
        if i == len(s) or j == len(t):
            return 1
        

        if s[i] == t[j]:
            return helper(i+1,j+1) + helper(i+1,j)
        else:
            return helper(i+1,j)
        
    return helper(0,0)







s1 = "rabbbit"
t1 = "rabbit"


s2 = "babgbag"
t2 = "bag"


print('With Recurrsion')
print(distinct_subsequences1(s1,t1))
print(distinct_subsequences1(s2,t2))