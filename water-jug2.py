def water_jug_dfs():
    jug1_capacity = 3
    jug2_capacity = 1
    target = 2

    # Stack contains (jug1, jug2, path)
    stack = [(0, 0, [])]

    visited = set()

    while stack:
        jug1, jug2, path = stack.pop()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Check target
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)]

        # Possible next states
        next_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2

            # Pour jug1 -> jug2
            (
                max(0, jug1 - (jug2_capacity - jug2)),
                min(jug2_capacity, jug1 + jug2)
            ),

            # Pour jug2 -> jug1
            (
                min(jug1_capacity, jug1 + jug2),
                max(0, jug2 - (jug1_capacity - jug1))
            )
        ]

        for state in next_states:
            if state not in visited:
                stack.append(
                    (state[0], state[1], path + [(jug1, jug2)])
                )

    return None


result = water_jug_dfs()

if result:
    print("Path to reach the target amount of water:")
    for step in result:
        print(step)
else:
    print("No solution found.")