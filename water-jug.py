from collections import deque


def water_jug_bfs(m, n, d):

    
    if d > max(m, n):
        return -1, []

    
    queue = deque([(0, 0, 0, [(0, 0)])])

    
    visited = [[False] * (n + 1) for _ in range(m + 1)]

    
    visited[0][0] = True

    while queue:

       
        jug1, jug2, steps, path = queue.popleft()

        
        if jug1 == d or jug2 == d:
            return steps, path

        

        states = [
            (m, jug2),       
            (jug1, n),       
            (0, jug2),       
            (jug1, 0),       

            
            (
                jug1 - min(jug1, n - jug2),
                jug2 + min(jug1, n - jug2)
            ),

            
            (
                jug1 + min(jug2, m - jug1),
                jug2 - min(jug2, m - jug1)
            )
        ]

        
        for new_jug1, new_jug2 in states:

            if not visited[new_jug1][new_jug2]:

                
                visited[new_jug1][new_jug2] = True

                
                new_path = path + [(new_jug1, new_jug2)]

                queue.append(
                    (new_jug1, new_jug2, steps + 1, new_path)
                )

    return -1, []



m = 3
n = 1
d = 2

steps, path = water_jug_bfs(m, n, d)

if steps != -1:

    print("Minimum number of steps:", steps)
    print("\nPath to reach the goal state:")

    for i, state in enumerate(path):
        print("Step", i, ":", state)

else:
    print("No solution")