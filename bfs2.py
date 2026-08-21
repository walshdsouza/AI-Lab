from collections import deque

def bfs(matrix, src):
   
    V = len(matrix)  
    visited = [False] * V
    result = []

    q = deque([src])
    visited[src] = True

    while q:
        u = q.popleft()
        result.append(u)
        for v in range(V):
            
            if matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                q.append(v)

    return result


V = 5 


matrix = [[0 for _ in range(V)] for _ in range(V)]

edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 4)
]

for u, v in edges:
    matrix[u][v] = 1  
    matrix[v][u] = 1 


src = 0 

result = bfs(matrix, src)

print("=== Adjacency Matrix BFS Result ===")
print("The Matrix looks like this:")
for row in matrix:
    print(row)

print(f"\nStarting vertex: {src}")
print("\nBFS Traversal Path:")
print(" -> ".join(map(str, result)))