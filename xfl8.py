import sys

def min_key(key, mst_set, V):
    """Utility function to find the vertex with the minimum key value."""
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v

    return min_index

def print_mst(parent, graph, V):
    """Utility function to print the constructed MST."""
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def prim_mst(graph):
    """Function to construct and print MST for a graph using Prim's algorithm."""
    V = len(graph)
    key = [sys.maxsize] * V  # Values used to pick minimum weight edge in cut
    parent = [None] * V  # Array to store the constructed MST
    key[0] = 0  # Make key 0 so that this vertex is picked as first vertex
    mst_set = [False] * V  # To represent set of vertices included in MST

    parent[0] = -1  # First node is always the root of MST

    for _ in range(V):
        # Pick the minimum distance vertex from the set of vertices not yet processed
        u = min_key(key, mst_set, V)

        # Add the picked vertex to the MST Set
        mst_set[u] = True

        # Update key value and parent index of the adjacent vertices of the picked vertex
        for v in range(V):
            if graph[u][v] > 0 and not mst_set[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph, V)

# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Print the solution
print("Minimum Spanning Tree using Prim's Algorithm:")
prim_mst(graph)
