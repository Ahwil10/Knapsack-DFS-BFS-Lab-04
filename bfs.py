from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
def bfs(graph, start_node):
    visited = {start_node}
    queue = deque([start_node])

    print("BFS Traversal starting from node A:")
    while queue:
        # Remove first node from queue and print it [cite: 10, 14]
        current_node = queue.popleft()
        print(current_node, end=" ")

        # Add all unvisited neighbors to the queue
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, 'A')
# Expected Output: A B C D E F
