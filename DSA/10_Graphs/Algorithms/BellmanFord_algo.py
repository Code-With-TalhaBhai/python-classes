
# Can find shortest path with negative weights also detect negative cycle

# Negative cycle is such a cycle on returning back to root it has negative weight. For such graph shortest path calculation is not possible.

edge_list1 = [[0,1,3],[0,2,5],[2,1,-3]]
edge_list2 = [[0,1,3],[1,2,5],[2,0,-6]] 
edge_list3 = [[0,1,1],[1,2,1],[2,0,-3]]# with negative cycle
edge_list4 = [[0,2,5],[0,1,3],[1,3,1],[2,4,2],[2,3,-3],[3,4,-2]]
# Directed graph with positive weights - match answer with digkstra's algorithm
edge_list5 = [["S","A",7],["S","B",2],["S","C",3],["A","S",7],["A","B",3],["A","D",4],["B","A",3],["B","D",4],["B","H",1],["B","S",2],["D","A",4],["D","B",4],["D","F",5],["H","B",1],["H","F",3],["H","G",2],["F","D",5],["F","H",3],["G","H",2],["G","E",2],["E","G",2],["E","K",5],["C","S",3],["C","L",2],["L","C",2],["L","I",4],["L","J",4],["I","J",6],["I","K",4],["I","L",4],["J","L",4],["J","I",6],["J","K",4],["K","I",4],["K","J",4],["K","E",5]]

# In Directed graphs also `Digkstras Algorithm` is preferred as it has time-complexiy of E log V far less than `BellmanFord` as it has time-complexity of E.V


# Also edge-list order doesn't matter
def bellmanFord(edge_list):
    weights = {}
    for u,v,w in edge_list:
        weights[u] = float("inf")
        weights[v] = float("inf")
    weights[0] = 0
    # weights["S"] = 0 # for directed-graph given above(as alphabets given as key)


    # relaxing edges n-1 times
    for i in range(len(weights)-1):
        for u,v,w in edge_list:
            if weights[u] + w < weights[v]:
                weights[v] = weights[u] + w 


    # relaxing one-more time to check if it has a negative cycle
    for u,v,w in edge_list:
        if weights[u] + w < weights[v]:
            return "Graph has negative cycle"

    return weights     


print(bellmanFord(edge_list1))
print(bellmanFord(edge_list2))
print(bellmanFord(edge_list3))
print(bellmanFord(edge_list4))
# print("Directed graph")
# print(bellmanFord(edge_list5))