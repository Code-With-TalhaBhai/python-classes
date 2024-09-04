

class DisjointSetUnion:
    def __init__(self,n):
        self.parent = list(range(n)) # [0,1,2,3,4] n = 5
        self.rank = [0]*n # [0,0,0,0,0]


    def find(self,x):
        # Simple parent-finding - Time-Complexity[O(n)]
        # if self.parent[x] != x:
        #     return self.find(self.parent[x])
        # return x
    
        # With path-compression - Time-Complexity[O(1)]  (first-time->Time-Complexity[O(n)])
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # path-compression
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        # Without union-rank -> High Time-complexity when Find()
        # if rootX != rootY:
        #     self.parent[rootY] = rootX

        # With Union-rank -> Low Time-complexity
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else: # equal-rank
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


DSU = DisjointSetUnion(5)
DSU.union(1,2)
DSU.union(3,4)
DSU.union(1,4)
DSU.union(0,3)


print(DSU.find(4))
print(DSU.find(3))
print(DSU.find(2))
print(DSU.find(1))
print(DSU.find(0))


                



