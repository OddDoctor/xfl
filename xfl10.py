from collections import deque

def is_bipartite(graph, start):
    """Check if the graph is bipartite using BFS."""
    colors = {}  # Dictionary to store colors of vertices
    queue = deque([start])
    colors[start] = 0  # Color the start vertex with color 0

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in colors:  # If neighbor has not been colored yet
                colors[neighbor] = 1 - colors[vertex]  # Assign opposite color to neighbor
                queue.append(neighbor)
            elif colors[neighbor] == colors[vertex]:  # If neighbor has the same color as vertex
                return False  # Graph is not bipartite

    return True  # Graph is bipartite

# Example graph represented as an adjacency list
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# Check if the graph is bipartite
start_vertex = 0
if is_bipartite(graph, start_vertex):
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
