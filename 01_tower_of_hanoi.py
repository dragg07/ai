def tower_of_hanoi(n, start_tower, end_tower, aux_tower):
    if n == 1:
        print(f"Move disk 1 from {start_tower} to {end_tower}")
        return
    
    tower_of_hanoi(n - 1, start_tower, aux_tower, end_tower)
    print(f"Move disk {n} from {start_tower} to {end_tower}")
    tower_of_hanoi(n - 1, aux_tower, end_tower, start_tower)

num_disks = int(input("Enter the number of disks: "))
start = input("Enter the name of the initial tower (e.g., A): ")
end = input("Enter the name of the final tower (e.g., C): ")
aux = input("Enter the name of the auxiliary tower (e.g., B): ")

print(f"Steps to move {num_disks} disks from {start} to {end}:")
tower_of_hanoi(num_disks, start, end, aux)
