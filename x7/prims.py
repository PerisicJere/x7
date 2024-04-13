import sys

def prim(graph):
    num_vertices = len(graph)
    mst = []
    visited = [False] * num_vertices

    visited[0] = True

    while len(mst) < num_vertices - 1:
        min_weight = sys.maxsize
        min_edge = None
        
        for i in range(num_vertices):
            if visited[i]:
                for j in range(num_vertices):
                    if not visited[j] and graph[i][j] != 0 and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        min_edge = (i, j, min_weight)
        
        if min_edge:
            source, dest, weight = min_edge
            mst.append((source, dest, weight))
            visited[dest] = True

    return mst

graphs = [
    [[0, 0.2, 0.16, 0.41],
    [0.2, 0, 9999999, 0.31],
    [0.16, 9999999, 0, 0.1],
    [0.41, 0.31, 0.1, 0]],
    [[0,3,8,4,6],
     [3,0,99999,99999,2],
     [8,99999,0,6,6],
     [4,99999,6,0,99999],
     [6,2,6,99999,0]
    ]
]
for graph in graphs:
    mst = prim(graph)

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)

