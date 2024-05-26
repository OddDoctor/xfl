def dfs_iterative(graph, start):
    """Perform DFS using an iterative approach."""
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            # Add adjacent nodes to the stack
            stack.extend(reversed(graph[vertex]))  # Reverse to maintain order

    print()  # For a new line

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Iterative DFS traversal:")
dfs_iterative(graph, 'A')
