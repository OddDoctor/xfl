from collections import deque

def bfs(graph, start):
    """Perform BFS on the graph starting from the start node."""
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print()  # For a new line

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}

print("BFS traversal:")
bfs(graph, 'A')
