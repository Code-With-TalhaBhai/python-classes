import heapq


def connect_n_ropes_with_min_cost(arr,n):
    cost = 0

    heapq.heapify(arr)
    # print(arr)

    while len(arr) > 1:
        min1 = heapq.heappop(arr)
        min2 = heapq.heappop(arr)

        # print("min1: ",min1)
        # print("min2: ",min2)

        sum = min1 + min2
        cost += sum
        heapq.heappush(arr,sum)

    return cost

    




n = 5
arr = [4, 2, 7, 6, 9]
print("The minimum cost of connecting ropes are: ",connect_n_ropes_with_min_cost(arr,n))