import sys

def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_distance = sys.maxsize
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        visited[min_index] = True

        for v in range(num_vertices):
            if not visited[v] and graph[min_index][v] != 0 and distances[min_index] + graph[min_index][v] < distances[v]:
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

graphs = [
    [[0,99999,99999,2,99999,99999],
    [99999,0,99999,99999,3,99999],
    [99999,99999,0,99999,99999,3],
    [99999,3,99999,3,0,5],
    [99999,99999,3,10,5,0]],
    [[0,99999,4,1,99999,99999,99999,99999,99999],
     [99999,0,99999,4,99999,99999,99999,99999,99999],
     [4,99999,0,99999,99999,2,99999,99999,99999],
     [1,4,99999,0,99999,99999,99999,99999,5],
     [99999,99999,99999,99999,0,9,8,99999,99999],
     [99999,99999,2,99999,9,0,99999,6,99999],
     [99999,99999,99999,99999,8,99999,0,99999,99999],
     [99999,99999,99999,99999,99999,6,99999,0,9],
     [99999,99999,99999,5,99999,99999,99999,9,0]]
]

for graph in graphs:
    start_vertex = 0
    distances = dijkstra(graph, start_vertex)

    print("Shortest distances from vertex", start_vertex, ":")
    for vertex, distance in enumerate(distances):
        print("Vertex:", vertex, "- Distance:", distance)
