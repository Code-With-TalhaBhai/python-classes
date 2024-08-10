from collections import defaultdict
import heapq

edge_list = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[2,4,7]]


adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))
    adjacency_list[v].append((u,w))
# print(adjacency_list)


def prims_algo(adjacency_list,src):
    # print(len(adjacency_list))
    mst = set()
    parents = []
    weight_track = {i:float("inf") for i in adjacency_list}
    min_heap = []
    heapq.heappush(min_heap,(src,0))
    mst.add(src)

    while len(mst) < len(adjacency_list):
        node,weight = heapq.heappop(min_heap)

        for neighbour,child_weight in adjacency_list[node]:
            total_weight = weight + child_weight
            if total_weight < weight_track[neighbour]:
                parents.append(neighbour)
                weight_track[neighbour] = total_weight
            heapq.heappush(min_heap,(total_weight,neighbour))
            mst.add(neighbour)

    return parents






print(prims_algo(adjacency_list,0))
