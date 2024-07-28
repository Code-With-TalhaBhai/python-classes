# Graph
Data Structure with combination of edges and vertices


## Types Of Graphs
    1. Undirected Graphs (without direction) === Degree -> No. of edges connected
    2. Directed Graphs (with direction)
       1. In-Degree(Number of edges comming inwards)
       2. Out-Degree(Number of edges comming outward)


#### Weighted Graphs(Can be Directed or UnDirected):
Having some weight value over the edge. If there is no weight, default weight is 1


### Cyclic or Acyclic Graphs:
        1. Cyclic Graphs:
           1. Cyclic Directed Graphs
           2. Cyclic Undirected Graphs
        2. Acyclic Graphs:
           1. Acyclic Directed Graphs
           2. Acyclic Undirected Graphs

## Representation of Graphs:
    1. Adjacency Matrix (2D Array)
    2. Ajacency List(Dictionary with arrays values)
    3. Class with `data` attribute as value and `neighbour` attribute as list of edges
   