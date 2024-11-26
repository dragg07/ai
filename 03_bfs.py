from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS traversal:", end=" ")
    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    # print()

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = input("Enter the starting node for BFS: ").strip().upper()

    if start_node in graph:
        bfs(graph, start_node)
    else:
        print("The starting node is not in the graph.")