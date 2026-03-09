# Adjacency List Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    # Mark node as visited and print it [cite: 8, 14]
    visited.add(start_node)
    print(start_node, end=" ")

    # Visit all unvisited neighbors
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("DFS Traversal starting from node A:")
dfs(graph, 'A')
