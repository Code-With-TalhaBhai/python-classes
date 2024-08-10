import heapq

def dijkstra(graph, start):
    # Create a priority queue to store (distance, node) tuples
    priority_queue = [(0, start)]
    # Initialize distances dictionary with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    # Distance to the start node is 0
    distances[start] = 0
    # Dictionary to track the shortest path
    shortest_path = {}
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If this distance is already greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path[neighbor] = current_node
    
    return distances, shortest_path

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, shortest_path = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")

# print(shortest_path)

# print("\nShortest Path Tree:")
# for node, previous in shortest_path.items():
    # print(f"Node {node} is reached from node {previous}")
