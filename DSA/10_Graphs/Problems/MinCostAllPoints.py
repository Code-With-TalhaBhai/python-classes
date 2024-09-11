import heapq

# Prim's Algorithm
def minCostConnectPoints1(points):
    min_heap = []
    heapq.heappush(min_heap,(0,0)) #(weight,index)
    
    visited = set()
    total_weight = 0


    # while len(visited) < len(points): # More Optimized
    while min_heap:
        weight,index = heapq.heappop(min_heap)

        if index not in visited:
            total_weight += weight
            visited.add(index)
            for j in range(len(points)):
                if j not in visited: # For optimization
                    abs_weight = abs(points[index][0] - points[j][0]) + abs(points[index][1] - points[j][1])
                    heapq.heappush(min_heap,(abs_weight,j))
    return total_weight    


class DSU:
    def __init__(self,n) -> None:
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def Union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootV] < self.rank[rootU]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


# Kruskal's Algorithm
def minCostConnectPoints2(points):
    n = len(points)
    dsu = DSU(n)
    heap_sorted = []
    total_weight = 0
    for i in range(len(points)):
        for j in range(i,len(points)):
            abs_weight = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
            heapq.heappush(heap_sorted,(abs_weight,i,j))

    visit = 0
    while heap_sorted:
    # while heap_sorted and visit < n-1: #For Optimization
        weight,u,v = heapq.heappop(heap_sorted)
        if dsu.find(u) != dsu.find(v):
            total_weight += weight
            dsu.Union(u,v)

    return total_weight





points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points2 = [[3,12],[-2,5],[-4,1]]
print("Through Prims Algorithm")
print(minCostConnectPoints1(points1))
print(minCostConnectPoints1(points2))

print("Through Kruskals Algorithm")
print(minCostConnectPoints2(points1))
print(minCostConnectPoints2(points2))