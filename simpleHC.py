import math


def objective(state):
    x, y = state
    return -0.5 * (x ** 2 + y ** 2) + 8 * math.cos(x) * math.cos(y)

def neighbors(state, step=0.5):
    x, y = state
    return [(x + dx, y + dy)
            for dx in (-step, 0, step)
            for dy in (-step, 0, step)
            if (dx, dy) != (0, 0)]

def simple_hill_climbing(objective, neighbors, start):
    current, current_val = start, objective(start)
    path = [(current, current_val)]
    while True:
        for n in neighbors(current):
            n_val = objective(n)
            if n_val > current_val:
                current, current_val = n, n_val
                path.append((current, current_val))
                break
        else:
            return path


x, y = [float(x) for x in input("Enter initial x and y: ").split()]
start = (x, y)
path = simple_hill_climbing(objective, neighbors, start)

print("Sequence of states:")
for i, (state, val) in enumerate(path):
    print(f"Step {i}: state = {state}, value = {val:.4f}")