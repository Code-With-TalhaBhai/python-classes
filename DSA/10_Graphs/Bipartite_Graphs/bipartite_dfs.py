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
    colors[0] = 0


    def dfs1(node):
        visited.add(node)
        for neighbour in adjacency_list[node]: 
            if colors[node] == colors[neighbour]:
                return False
            else:
                if colors[neighbour] == -1:
                    if colors[node] == 0:
                        colors[neighbour] = 1
                    elif colors[node] == 1:
                        colors[neighbour] = 0
            
            if neighbour not in visited:
                if not dfs1(neighbour):
                    return False

        return True



    def dfs2(node,color):
        colors[node] = color

        for neighbour in adjacency_list[node]:
            if colors[neighbour] == -1:
                if not dfs2(neighbour,1-color):
                    return False
                
            # elif colors[neighbour] == colors[node]:
            elif colors[neighbour] == color:
                return False
            
                
        return True



    # result = dfs1(0) # by-me
    result = dfs2(0,0) # shorter-code

    if result == True:
        print("Its a bipirtite graph")
    else:
        print("Its not a bipirtite graph")


check_bipartite(edge_list1) # Not a bipartite graph
check_bipartite(edge_list2)
check_bipartite(edge_list3) # Not a bipartite graph