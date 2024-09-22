from collections import defaultdict

# assign the color to the next node not same

edge_list1 = [(0,1),(0,2),(0,3),(1,2),(2,3)]
edge_list2 = [(0,1),(0,4),(0,5),(0,10),(1,2),(1,3),(1,4),(2,3),(3,4),(3,5),(3,8),(3,9),(5,6),(5,7),(6,7),(8,9),(10,11),(10,12),(11,12)]
edge_list3 = [(0,1),(0,2),(1,2)]

def m_coloring(edge_list,m):
    colors = {}
    adjacency_list = defaultdict(list)
    for u,v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        colors[u] = -1
        colors[v] = -1


    def dfs(node,color):
        last_color = color
        for neighbours in adjacency_list[node]:
            if colors[neighbours] == -1:
                continue

        colors[node] = color


        for neighbours in adjacency_list[node]:
            if colors[neighbours] == -1:
                color = (color+1)%m
                if not dfs(neighbours,color):
                    return False
            elif colors[node] == colors[neighbours]:
                # colors[node] = -1
                return False
            
        return True

    # return dfs(0,0)
    dfs(0,0)
    print(colors)


print(m_coloring(edge_list1,3)) # 3-color