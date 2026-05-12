# Artificial Intelligence Practical 1
# Implementation of DFS and BFS (Recursive) for Undirected Graph

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Recursive Depth First Search
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

# Recursive Breadth First Search
def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    node = queue.pop(0)
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    bfs(graph, queue, visited)

# Driver Code
print("Graph Representation:", graph)

print("\nDepth First Search (DFS) Traversal:")
dfs(graph, 'A')

print("\n\nBreadth First Search (BFS) Traversal:")
bfs(graph, ['A'])