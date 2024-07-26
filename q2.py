import heapq
def dijkstra(graph,source):
    distances = {vertex:float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0,source)]
    while priority_queue:
        curr_dist,curr_vertex = heapq.heappop(priority_queue)
        if curr_dist>distances[curr_vertex]:
            continue
        for neighbor, weight in graph[curr_vertex].items():
            dist = curr_dist+weight
            if dist<distances[neighbor]:
                distances[neighbor]= dist
                heapq.heappush(priority_queue,(dist,neighbor))
    return distances            
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}

source = 0
print(dijkstra(graph,source))