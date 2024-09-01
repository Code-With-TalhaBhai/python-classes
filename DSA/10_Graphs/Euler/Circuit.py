# Path is Eulerian-Circuit if it is a eulerian-path and its starting and ending node is same

# 1. All non-zero degree nodes should be connected
# 2. All nodes should have even degree


from collections import defaultdict
edge_list1 = [(0,1),(0,2),(0,3),(1,2),(3,4)]
edge_list2 = [(0,1),(0,2),(0,3),(0,4),(1,2),(3,4)]


def check_euler_circuit(edge_list):
    adjacency_list = defaultdict(list)
    for u,v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)


    for node in adjacency_list:
        if len(adjacency_list[node]) == 1:
            print("Not a Euler Circuit")
            return


    # checking connected or not
    visited = set()
    visited.add(0)
    def dfs(node):
        visited.add(node)
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                dfs(neighbour)


    for i in adjacency_list:
        if i in visited:
            dfs(i)
        else:
            print("Not a circuit")
        

    print("Its a Euler Circuit")




check_euler_circuit(edge_list1)
check_euler_circuit(edge_list2)