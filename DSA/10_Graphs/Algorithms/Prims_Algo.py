from collections import defaultdict
import heapq

edge_list = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[2,4,7]]


adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))
    adjacency_list[v].append((u,w))
# print(adjacency_list)


def prims_algo1(adjacency_list,src):
    mst = set()
    parents = {}
    min_heap = []
    heapq.heappush(min_heap,(0,src,-1))
    total_weight = 0


    while min_heap:
        weight,node,parent = heapq.heappop(min_heap)

        mst.add(node)
        parents[node] = parent
        total_weight += weight



    return {'mst':parents,'weight':total_weight}





def prims_algo2(adjacency_list,src):
    mst = set()
    parents = {}
    min_heap = []
    heapq.heappush(min_heap,(0,src,-1))
    total_weight = 0


    while len(mst) < len(adjacency_list):
        weight,node,parent = heapq.heappop(min_heap)
        parents[node] = parent
        mst.add(node)
        wei += weight

        for neighbour,child_weight in adjacency_list[node]:
            if neighbour not in mst:
                heapq.heappush(min_heap,(child_weight,neighbour,node))

    return {'mst':parents,'weight':total_weight}


print(prims_algo1(adjacency_list,0))
print(prims_algo2(adjacency_list,0)) # More efficient
