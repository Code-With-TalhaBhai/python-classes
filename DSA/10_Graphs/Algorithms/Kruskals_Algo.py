# No need of adjacency_list

edge_list = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[2,4,7]]

def heapify(arr,i,n):
    
    left = (2 * i) + 1
    right = (2 * i) + 2
    smallest = i

    if left < n and arr[left][2] > arr[smallest][2]:
        smallest = left
    if right < n and arr[right][2] > arr[smallest][2]:
        smallest = right

    if i != smallest:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,smallest,n)

    


def heap_sorted(edge_list,n):

    # max-heapify
    for i in range(n//2,-1,-1):
        heapify(edge_list,i,n)

    for i in range(n-1,0,-1):
        edge_list[0],edge_list[i] = edge_list[i],edge_list[0]
        heapify(edge_list,0,i)
    return edge_list


class DSU:

    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [False]*n

    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def Union(self,u,v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootV] < self.rank[rootU]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
        



def kruskal_algo(edge_list):
    n = len(edge_list)
    heap_sort = heap_sorted(edge_list,n)
    # to find number of edges
    nodes = set()
    for item in edge_list:
        nodes.add(item[0])
        nodes.add(item[1])

    n = len(nodes)
    dsu = DSU(n)

    # real algorithm
    total_weight = 0
    mst = []
    for u,v,weight in heap_sort:
        if dsu.find(u) != dsu.find(v):
            total_weight += weight
            mst.append((u,v))
            dsu.Union(u,v)

    return {'mst':mst,'weight':total_weight}


print(kruskal_algo(edge_list))