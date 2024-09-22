from collections import defaultdict

edge_list1 = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
edge_list2 = [(0,1),(0,3),(0,5),(1,2),(2,3),(3,4)]

def make_adjacency_list(edge_list):
    adjacency_list = defaultdict(list)
    for u,v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def hamiltonian_path(adjacency_list,start_node):
    n = len(adjacency_list)
    path = []
    visited = set()


    def find_path(node):
        visited.add(node)
        path.append(node)
        if len(path) == n:
            return True

        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                if find_path(neighbour):
                    return True

        visited.remove(node)
        path.remove(node)
        return False

            
    find_path(start_node)
    check = True
    if len(adjacency_list) != len(path):
        check = False
    return [check,path]


adj_list1 = make_adjacency_list(edge_list1)
adj_list2 = make_adjacency_list(edge_list2)
print(hamiltonian_path(adj_list1,0))
print(hamiltonian_path(adj_list2,0))
print(hamiltonian_path(adj_list2,5))

print()
print()


def check_from_all_nodes(edge_list):
    adj_list = make_adjacency_list(edge_list)

    for starting_node in adj_list:
        check = hamiltonian_path(adj_list,starting_node)
        if check[0]:
            return check[1]

    return "Not a hamiltanion path"

print(check_from_all_nodes(edge_list1))
print(check_from_all_nodes(edge_list2))



