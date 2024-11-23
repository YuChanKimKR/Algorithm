import heapq

def array_to_tuple(arr):
    return tuple(arr)

def dijkstra(initial, target, manipulations):
    queue = []
    heapq.heappush(queue, (0, initial))
    visited = {initial: 0}

    while queue:
        current_cost, current_state = heapq.heappop(queue)

        if current_state == target:
            return current_cost

        if visited[current_state] < current_cost:
            continue

        for l, r, c in manipulations:
            new_state = list(current_state)
            new_state[l], new_state[r] = new_state[r], new_state[l]
            new_state = array_to_tuple(new_state)
            new_cost = current_cost + c

            if new_state not in visited or new_cost < visited[new_state]:
                visited[new_state] = new_cost
                heapq.heappush(queue, (new_cost, new_state))

    return -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    array = list(map(int, data[index:index + N]))
    index += N
    M = int(data[index])
    index += 1
    manipulations = []
    for _ in range(M):
        l = int(data[index]) - 1
        r = int(data[index + 1]) - 1
        c = int(data[index + 2])
        manipulations.append((l, r, c))
        index += 3

    initial_state = array_to_tuple(array)
    target_state = array_to_tuple(sorted(array))

    result = dijkstra(initial_state, target_state, manipulations)
    print(result)

if __name__ == "__main__":
    main()