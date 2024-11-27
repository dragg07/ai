import random

def hill_climbing(start, step_size, max_iterations):
    def objective_function(x):
        return -(x - 3) ** 2 + 9  # Maximum value is 9 at x = 3

    current_solution = start
    current_value = objective_function(current_solution)
    print(f"Starting point: x = {current_solution}, f(x) = {current_value}")
    for i in range(max_iterations):
        neighbor = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor)
        print(f"Iteration {i+1}: x = {neighbor:.4f}, f(x) = {neighbor_value:.4f}")
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            print(f" -> New best solution: x = {current_solution:.4f}, f(x) = {current_value:.4f}")

    print("\nBest solution found:")
    print(f"x = {current_solution:.4f}, f(x) = {current_value:.4f}")
    return current_solution

if __name__ == "__main__":
    start_point = float(input("Enter a starting point: "))
    step_size = 0.5
    max_iters = 20
    hill_climbing(start_point, step_size, max_iters)