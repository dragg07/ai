from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))

    path = {}

    while queue:
        current = queue.popleft()
        jug1, jug2 = current

        if jug1 == target or jug2 == target:
            solution = []
            while current in path:
                solution.append(current)
                current = path[current]
            solution.append((0, 0))
            return solution[::-1]

        possible_states = [
            (jug1_capacity, jug2),          
            (jug1, jug2_capacity),
            (0, jug2),                     
            (jug1, 0),                     
            (jug1 - min(jug1, jug2_capacity - jug2), 
             jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1), 
             jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                path[state] = current

    return None

if __name__ == "__main__":
    jug1 = int(input("Enter the capacity of Jug 1: "))
    jug2 = int(input("Enter the capacity of Jug 2: "))
    target = int(input("Enter the target amount of water: "))

    solution = water_jug_problem(jug1, jug2, target)
    if solution:
        print("\nSteps to measure the target amount:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")