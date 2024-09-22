# An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all. 
# leetcode 1489
from collections import defaultdict
import heapq
from logging import critical


class DSU:

    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [False]*n

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



def findCriticalAndPseudoCriticalEdges(n,edges):

    def mst(edge_list,idx,forced_edge=None):
        dsu = DSU(n)
        min_heap = []
        for index,edge in enumerate(edge_list):
            # print(index)
            if index == idx:
                continue
            u,v,w = edge
            heapq.heappush(min_heap,(w,u,v))

        mst_weight = 0
        count_edges = 0

        if forced_edge is not None:
            u,v,w = edge_list[forced_edge]
            if dsu.find(u) != dsu.find(v):
                dsu.Union(u,v)
                mst_weight += w
                count_edges += 1
        
        while min_heap:
            weight,parent,child = heapq.heappop(min_heap)
            if dsu.find(parent) != dsu.find(child):
                mst_weight += weight
                dsu.Union(parent,child)
                count_edges += 1

        return mst_weight if count_edges == n-1 else -1
    

    original_mst = mst(edges,-1)
    print(original_mst)

    def find_critical_edges():
        critical_edges = []

        for i in range(len(edges)):
            if original_mst < mst(edges,i):
                critical_edges.append(i)
        return critical_edges

    def find_pseudo_critical_edges():
        pseudo_critical_edges = []
        for i in range(len(edges)):
            if original_mst == mst(edges,-1,i):
                # print(i)
                pseudo_critical_edges.append(i)
        return pseudo_critical_edges

    # print(find_critical_edges())
    # print(find_pseudo_critical_edges())
    return [find_critical_edges(),find_pseudo_critical_edges()]

    


edges1 = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
edges2 = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]


print(findCriticalAndPseudoCriticalEdges(5,edges1))
print(findCriticalAndPseudoCriticalEdges(4,edges2))