import itertools
import sys

def tsp_brute_force(graph):
    """Solve the Traveling Salesperson Problem (TSP) using brute-force approach."""
    num_cities = len(graph)
    min_cost = sys.maxsize
    min_path = None

    # Generate all possible permutations of cities to visit
    permutations = itertools.permutations(range(num_cities))

    # Iterate through each permutation
    for path in permutations:
        # Calculate the total cost of the current path
        cost = 0
        for i in range(num_cities):
            cost += graph[path[i-1]][path[i]]  # Distance between consecutive cities
        cost += graph[path[num_cities-1]][path[0]]  # Return to the starting city

        # Update minimum cost and path if needed
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_cost, min_path

# Example graph represented as an adjacency matrix
# graph[i][j] represents the distance from city i to city j
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve the TSP and print the result
min_cost, min_path = tsp_brute_force(graph)
print(f"Minimum Cost: {min_cost}")
print(f"Optimal Path: {min_path}")
