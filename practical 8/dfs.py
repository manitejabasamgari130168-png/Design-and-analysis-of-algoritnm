# DFS using user input

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

visited = set()

def dfs(node):
    print(node, end=" ")
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

print("DFS Traversal:")
dfs(start)