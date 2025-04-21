

def findContentChildren(g, s) -> int:

    g.sort()
    s.sort()

    j = 0
    for i in range(len(s)):
        if s[i] >= g[j]:
            j += 1
        if j == len(g):
            return j
    return j





g1 = [1,2,3]
s1 = [1,1]
g2 = [1,2]
s2 = [1,2,3]
g3 = [1,2,3]
s3 = [3]

print(findContentChildren(g1,s1))
print(findContentChildren(g2,s2))
print(findContentChildren(g3,s3))