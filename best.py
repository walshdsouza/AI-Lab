import heapq

def best(graph, heuristics, start, goal):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristics[start], start))

    parent = {start: None}
    
    while pq:
        current_h, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        if current_node == goal:
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            
            print(f"Goal reached! Path taken: {' -> '.join(path)}")
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current_node
                heapq.heappush(pq, (heuristics[neighbor], neighbor))
                
    print("Goal not found.")
    return []

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'G'],
    'B': ['S', 'G'],
    'C': ['A', 'G'],
    'G': ['A', 'B', 'C']
}

heuristics = {
    'S': 10,
    'A': 8,
    'B': 2,
    'C': 4,
    'G': 0
}

best(graph, heuristics, start='S', goal='G')