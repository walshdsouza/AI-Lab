from collections import deque

def bfs(graph, S):
    n = len(graph)
    visited = [False] * n
    Q = deque()

    visited[S] = True
    Q.append(S)

    while Q:
        u = Q.popleft()
        print(u, end=" ")

        for v in range(n):
            if graph[u][v] == 1 and visited[v] == False:
                visited[v] = True
                Q.append(v)


# Graph
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

S = 0
bfs(graph, S)

