from collections import defaultdict


edge_list = [[1,2],[2,3],[4,5],[5,6],[5,7],[6,8],[7,8],[8,9]]


def make_adjacency_list(edge_list):
    adj_list = defaultdict(list)
    for u,v in edge_list:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


class DisjointUnionSet:
    
    def __init__(self,n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n


    def find(self,x):
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootY] < self.rank[rootX]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


    def detect_cycle(self,adjacency_list):
        # print(adjacency_list)
        visited = {i:False for i in adjacency_list}
        # print(visited)
        for edge in adjacency_list:
            for vertex in adjacency_list[edge]:
                if visited[vertex] == True:
                    continue
                if self.find(edge) == self.find(vertex):
                    # print(edge,' ',vertex)
                    return True
                self.union(edge,vertex)
            visited[edge] = True
        return False


def check_cycle(cycle):
    if cycle:
        print("cycle detected")
    else:
        print("No cycle detected")



adjacency_list = make_adjacency_list(edge_list)


DSU = DisjointUnionSet(10)
check_cycle(DSU.detect_cycle(adjacency_list))