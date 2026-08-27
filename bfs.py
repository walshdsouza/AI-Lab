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

        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                Q.append(v)


# Graph
graph = [
    [1, 2],       # 0 is connected to 1, 2
    [0, 3, 4],    # 1 is connected to 0, 3, 4
    [0, 5],       # 2 is connected to 0, 5
    [1],          # 3 is connected to 1
    [1, 5],       # 4 is connected to 1, 5
    [2, 4]        # 5 is connected to 2, 4
]

S = 0
bfs(graph, S)

