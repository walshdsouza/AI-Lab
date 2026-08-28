from collections import deque


def water_jug_bfs(m, n, d):

    # If target is greater than both jug capacities
    if d > max(m, n):
        return -1, []

    # Queue stores (jug1, jug2, steps, path)
    queue = deque([(0, 0, 0, [(0, 0)])])

    # 2D visited array
    visited = [[False] * (n + 1) for _ in range(m + 1)]

    # Mark initial state as visited
    visited[0][0] = True

    while queue:

        # Remove front element
        jug1, jug2, steps, path = queue.popleft()

        # Check if target is reached
        if jug1 == d or jug2 == d:
            return steps, path

        # Generate all possible states

        states = [
            (m, jug2),       # Fill Jug 1
            (jug1, n),       # Fill Jug 2
            (0, jug2),       # Empty Jug 1
            (jug1, 0),       # Empty Jug 2

            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, n - jug2),
                jug2 + min(jug1, n - jug2)
            ),

            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, m - jug1),
                jug2 - min(jug2, m - jug1)
            )
        ]

        # Process generated states
        for new_jug1, new_jug2 in states:

            if not visited[new_jug1][new_jug2]:

                # Mark as visited
                visited[new_jug1][new_jug2] = True

                # Add new state and path to queue
                new_path = path + [(new_jug1, new_jug2)]

                queue.append(
                    (new_jug1, new_jug2, steps + 1, new_path)
                )

    return -1, []


# Example
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