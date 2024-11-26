def ao_star(node, graph, heuristic, solved):
    if solved[node]:
        return heuristic[node]

    print(f"Expanding node: {node}")

    if node not in graph or not graph[node]:
        solved[node] = True
        return heuristic[node]

    min_cost = float('inf')
    best_subgraph = None

    for subgraph in graph[node]:
        cost = 0
        for sub_node in subgraph:
            cost += ao_star(sub_node, graph, heuristic, solved)
        if cost < min_cost:
            min_cost = cost
            best_subgraph = subgraph

    heuristic[node] = min_cost
    solved[node] = all(solved[sub_node] for sub_node in best_subgraph)
    return heuristic[node]

if __name__ == "__main__":
    graph = {
        'A': [['B', 'C'], ['D']],  # A has two options: [B and C] (AND) or [D] (OR)
        'B': [['E'], ['F']],       # B has two options: [E] (OR) or [F] (OR)
        'C': [['G']],              # C has one option: [G] (OR)
        'D': [],                   # D is a terminal node
        'E': [],                   # E is a terminal node
        'F': [],                   # F is a terminal node
        'G': []                    # G is a terminal node
    }

    heuristic = {
        'A': float('inf'),
        'B': 1,
        'C': 1,
        'D': 3,
        'E': 2,
        'F': 4,
        'G': 1
    }

    solved = {node: False for node in heuristic}

    print("\nStarting AO* algorithm:")
    cost = ao_star('A', graph, heuristic, solved)
    print(f"\nOptimal cost to solve the problem: {cost}")
