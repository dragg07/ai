import heapq

def a_star_algorithm(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (cost, node)

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    came_from = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], g_cost[goal]

        for neighbor, cost in graph[current_node].items():
            new_cost = g_cost[current_node] + cost
            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'D': 2, 'E': 4},
        'C': {'A': 3, 'F': 2},
        'D': {'B': 2, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 3},
        'F': {'C': 2, 'E': 3}
    }

    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 3,
        'E': 1,
        'F': 0 #goal
    }

    start_node = input("Enter the starting node: ").strip().upper()
    goal_node = input("Enter the goal node: ").strip().upper()

    if start_node in graph and goal_node in graph:
        path, cost = a_star_algorithm(graph, start_node, goal_node, heuristic)
        if path:
            print(f"Shortest path: {' -> '.join(path)}")
            print(f"Total cost: {cost}")
        else:
            print("No path found.")
    else:
        print("Invalid starting or goal node.")
