

# In_Code
# If nodes adjacent nodes have different colour then it is going to be bipartite graph
# We can denote colours be red,blue be 0,1. Initially, it has no colour which is -1


from collections import defaultdict, deque


edge_list1 = [(0,1),(0,2),(1,2)]
edge_list2 = [(0,1),(1,2),(2,3),(2,7),(3,4),(4,5),(5,6),(5,8),(6,7)]
edge_list3 = [(0,1),(1,2),(1,3),(3,4),(3,5),(3,8),(5,6),(6,7),(7,8)]



def check_bipartite(edge_list):
    adjacency_list = defaultdict(list)
    for u,v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)


    colors = {node:-1 for node in adjacency_list}
    visited = set()

    source = 0
    dq = deque()
    dq.append(source)
    visited.add(source)
    colors[source] = 0


    while dq:
        node = dq.popleft()

        for neighbours in adjacency_list[node]:
            if neighbours not in visited:
                dq.append(neighbours)
                visited.add(neighbours)

            if colors[node] == colors[neighbours]:
                print("Not a bipirtite graph")
                return
            else:
                if colors[node] == 1:
                    colors[neighbours] = 0
                else:
                    colors[neighbours] = 1


    print("Its bipirtite graph")



check_bipartite(edge_list1)
check_bipartite(edge_list2)
check_bipartite(edge_list3)