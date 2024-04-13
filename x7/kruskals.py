def kruskal(graph):
    num_vertices = len(graph)
    edges = []

    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if graph[u][v] != 0:
                edges.append((graph[u][v], u, v))

    edges.sort()

    mst = []
    parent = [i for i in range(num_vertices)]

    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u

    def union(u, v):
        pu, pv = find(u), find(v)
        parent[pv] = pu

    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst
# exercise 1, and 2 random graphs
graphs = [[[0,32,99999,17,99999,99999,99999,99999,99999,99999],
           [32,0,99999,99999,45,99999,99999,99999,99999,99999],
           [99999,99999,0,18,99999,99999,5,99999,99999,99999],
           [17,99999,18,0,10,99999,99999,3,99999,99999],
           [99999,45,99999,10,0,28,99999,99999,25,99999],
           [99999,99999,99999,99999,28,0,99999,99999,99999,6],
           [99999,99999,5,99999,99999,99999,0,59,99999,99999],
           [99999,99999,99999,3,99999,99999,59,0,4,99999],
           [99999,99999,99999,99999,99999,99999,99999,4,0,12],
           [99999,99999,99999,99999,99999,6,99999,99999,12,0]],
    [[0,6,6,8],
     [6,0,5,3],
     [6,5,0,10],
     [8,3,10,0]
     ],
     [[0,8,4,3,99999],
      [8,0,3,3,99999],
      [4,3,0,9,5],
      [3,3,9,0,2],
      [99999,99999,5,2,0]]
]
for graph in graphs:
    mst = kruskal(graph)

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
