# 1. Make min_heap and add all elements(neighbour) of the node
# 2. Pop out all the elements one-by-one
# 3. Add their neighbours to the min_heap expcept those which are already visited

from collections import defaultdict
import heapq

edge_list = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[2,4,7]]


adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))
    adjacency_list[v].append((u,w))
# print(adjacency_list)


def prims_algo1(adjacency_list,src):
    visited = set()
    min_heap = []
    heapq.heappush(min_heap,(0,src,-1)) # (weight,node,parent)
    total_weight = 0
    parents = {}

    while min_heap:
        # print(min_heap)
        weight,node,parent = heapq.heappop(min_heap)
        
        if node not in visited:
            total_weight += weight
            visited.add(node)
            for neighbour,child_weight in adjacency_list[node]:
                parents[node] = parent
                heapq.heappush(min_heap,(child_weight,neighbour,node))

    return {'mst':parents,'total_weight':total_weight} 





def prims_algo2(adjacency_list,src):
    visited = set()
    parents = {}
    min_heap = []
    heapq.heappush(min_heap,(0,src,-1))
    total_weight = 0


    while len(visited) < len(adjacency_list):
        weight,node,parent = heapq.heappop(min_heap)
        parents[node] = parent
        visited.add(node)
        total_weight += weight

        for neighbour,child_weight in adjacency_list[node]:
            if neighbour not in visited:
                heapq.heappush(min_heap,(child_weight,neighbour,node))

    return {'mst':parents,'weight':total_weight}


print(prims_algo1(adjacency_list,0)) # original 
print(prims_algo2(adjacency_list,0)) # More efficient
