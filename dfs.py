def dfs(adj, src):
    
    V = len(adj)
    visited = [False] * V
    result = []
    stack = [src]
    
    while stack:
        u = stack.pop()
        
        if not visited[u]:
            visited[u] = True
            result.append(u)
            
            
            for v in reversed(adj[u]):
                if not visited[v]:
                    stack.append(v)
                    
    return result

def count(adj, src):
    
    return len(adj[src])



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

print(f"Graph Edges: {edges}\n")

start_vertex = 0
traversal_order = dfs(adj, start_vertex)
print(f"DFS Traversal Path (Starting at {start_vertex}): {' -> '.join(map(str, traversal_order))}")


print("\n--- Connection Checker ---")
node_to_check = int(input(f"Enter the vertex to check connections (0-{V-1}): "))


if 0 <= node_to_check < V:
    direct_count = count(adj, node_to_check)
    print(f"Node {node_to_check} is connected to {direct_count} vertices.")
    print(f"These neighbors are: {adj[node_to_check]}")
else:
    print("Invalid vertex! Please enter a number within the graph's range.")