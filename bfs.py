from collections import deque

def bfs(adj, src):
    V = len(adj)
    visited = [False] * V
    result = []

    q = deque([src])
    visited[src] = True

    while q:
        u = q.popleft()
        result.append(u)

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return result


V = 5  


adj = [[] for _ in range(V)]


edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 4)
]


for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)  


src = 0 

result = bfs(adj, src)

print("=== Hard-Coded BFS Result ===")
print(f"Edges in graph: {edges}")
print(f"Starting vertex: {src}")
print("\nBFS Traversal Path:")
print(" -> ".join(map(str, result)))