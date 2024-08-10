from collections import defaultdict
import heapq



# In-Progress
def network_delay(times,dest,src):
    adjacency_list = defaultdict(list)
    for sender,receiver,time in times:
        adjacency_list[sender].append((receiver,time))
        adjacency_list[receiver]

    min_heap = []
    heapq.heappush(min_heap,(0,src))
    shortest_travel_time = {i:float("inf") for i in adjacency_list}
    shortest_travel_time[src] = 0

    while min_heap:
        # print(shortest_travel_time)
        current_time,network = heapq.heappop(min_heap)

        # if network == dest:
        #     if shortest_travel_time[network] == 0:
        #         return -1
        #     return shortest_travel_time[network]
        
        for neighbour,time in adjacency_list[network]:
            total_time = current_time + time
            if total_time < shortest_travel_time[neighbour]:
                shortest_travel_time[neighbour] = total_time
                heapq.heappush(min_heap,(total_time,neighbour))

    # print(shortest_travel_time)
    return -1 if shortest_travel_time[network] == 0  else shortest_travel_time[network]
    # return -1 if shortest_travel_time[dest] == 0  else shortest_travel_time[dest]
    # print(shortest_travel_time)
    # return shortest_travel_time[network]
    


times = [[2,1,1],[2,3,1],[3,4,1]]
print(network_delay(times,4,2))


times = [[1,2,1]]
print(network_delay(times,2,2))


times = [[1,2,1],[2,1,3]]
print(network_delay(times,2,2))


times = [[1,2,1],[2,3,2],[1,3,1]]
print(network_delay(times,3,2))
