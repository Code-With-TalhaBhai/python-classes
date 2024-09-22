from collections import defaultdict
import heapq

    

graph = [
    ["S","A",7],
    ["S","B",2],
    ["S","C",3],
    ["A","S",7],
    ["A","B",3],
    ["A","D",4],
    ["B","A",3],
    ["B","D",4],
    ["B","H",1],
    ["B","S",2],
    ["D","A",4],
    ["D","B",4],
    ["D","F",5],
    ["H","B",1],
    ["H","F",3],
    ["H","G",2],
    ["F","D",5],
    ["F","H",3],
    ["G","H",2],
    ["G","E",2],
    ["E","G",2],
    ["E","K",5],
    ["C","S",3],
    ["C","L",2],
    ["L","C",2],
    ["L","I",4],
    ["L","J",4],
    ["I","J",6],
    ["I","K",4],
    ["I","L",4],
    ["J","L",4],
    ["J","I",6],
    ["J","K",4],
    ["K","I",4],
    ["K","J",4],
    ["K","E",5]
]


adjacency_list = defaultdict(list)
for u,v,w in graph:
    adjacency_list[u].append((v,w))
# print(adjacency_list)


def digkstras_algo1(adjacency_list,src,dest):

    min_heap = []
    heapq.heappush(min_heap,(0,src))

    # shortest_paths = {i:float("inf") for i in adjacency_list}
    shortest_paths = {}
    shortest_paths[src] = 0
    # print(shortest_paths)

    node = src
    while node != dest:
        weight,node = heapq.heappop(min_heap)
        if node not in shortest_paths:
            shortest_paths[node] = float("inf")

        if shortest_paths[node] > weight:
            shortest_paths[node] = weight

        for neighbour,sub_weight in adjacency_list[node]:
            total_weight = weight + sub_weight
            heapq.heappush(min_heap,(total_weight,neighbour))
    return shortest_paths


def digkstras_algo2(adjacency_list,src):
        
    min_heap = []
    heapq.heappush(min_heap,(0,src))

    shortest_paths = {i:float("inf") for i in adjacency_list}
    shortest_paths[src] = 0


    while min_heap:
        weight,node = heapq.heappop(min_heap)
        # network_delaynetwork_delayprint(weight,node)

        # To save additional iterations as it were added in heap before when it was shortest path
        if weight > shortest_paths[node]:
            # print("weight",weight)
            # print("node",node)
            # print("path",shortest_paths[node])
            continue

        for neighbour,subweight in adjacency_list[node]:
            # print(subweight,neighbour)
            total_weight = weight + subweight
            if total_weight < shortest_paths[neighbour]:
                shortest_paths[neighbour] = total_weight
                heapq.heappush(min_heap,(total_weight,neighbour))

    return shortest_paths






src = "S"
dest = "E"
# For Source to Destination - bY ME
# print(digkstras_algo1(adjacency_list,src,dest))
# For Every Single Path - Original
print(digkstras_algo2(adjacency_list,src))