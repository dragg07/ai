import random

def generate_neighbors(x, step_size=1, num_neighbors=10):
    return [x + random.uniform(-step_size, step_size) for _ in range(num_neighbors)]

def hill_climbing(f, x0, step_size=1, num_neighbors=10):
    x = x0
    while True:
        neighbors = generate_neighbors(x, step_size, num_neighbors)
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):
            return x
        
        x = best_neighbor

if __name__ == "__main__":
    def objective_function(x):
        return -(x - 3) ** 2 + 9  # Maximum value is 9 at x = 3

    start_point = float(input("Enter the starting point: "))
    best_solution = hill_climbing(objective_function, start_point, step_size=0.5, num_neighbors=20)

    print(f"Best solution found: x = {best_solution:.4f}, f(x) = {objective_function(best_solution):.4f}")