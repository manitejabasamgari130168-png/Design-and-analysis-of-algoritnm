from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
queue = deque()

start = input("Enter starting node: ")

queue.append(start)

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            queue.append(neighbour)