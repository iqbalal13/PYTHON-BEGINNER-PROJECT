num_cubes = int(input("Enter the number of cubes: "))

total_volume = 0
for i in range(num_cubes):
    side_length = float(input(f"Enter the side length of cube {i + 1}: "))
    total_volume += side_length ** 3

print(f"\nThe total volume of all cubes is: {total_volume}")