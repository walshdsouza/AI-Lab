def dfs(adj, n, start):
    visited = [False] * n
    stack = []
    stack.append(start)

    print("DFS Traversal:", end=" ")

    while len(stack) != 0:
        u = stack.pop()

        if visited[u] == False:
            visited[u] = True
            print(u, end=" ")

            for v in reversed(adj[u]):
                if visited[v] == False:
                    stack.append(v)


def check_path(adj, n, v1, v2):
    visited = [False] * n
    stack = []
    stack.append(v1)

    while len(stack) != 0:
        u = stack.pop()

        if visited[u] == False:
            visited[u] = True

            if u == v2:
                return True

            for v in adj[u]:
                if visited[v] == False:
                    stack.append(v)

    return False


def count_neighbours(adj, node):
    count = len(adj[node])
    return count


n = int(input("Enter number of vertices: "))

adj = []

for i in range(n):
    print("Enter adjacent vertices of vertex", i, "separated by space:")
    vertices = list(map(int, input().split()))
    adj.append(vertices)


start = int(input("\nEnter starting vertex for DFS: "))
dfs(adj, n, start)


v1 = int(input("\n\nEnter first vertex: "))
v2 = int(input("Enter second vertex: "))

if check_path(adj, n, v1, v2):
    print("Path exists between", v1, "and", v2)
else:
    print("No path exists between", v1, "and", v2)


node = int(input("\nEnter vertex to count neighbouring vertices: "))
count = count_neighbours(adj, node)

print("Number of vertices connected to", node, "=", count)