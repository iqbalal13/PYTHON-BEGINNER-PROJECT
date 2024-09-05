def cube_volume(side_length):
    return side_length ** 3

def main():
    num_cubes = int(input("Enter the number of cubes: "))

    total_volume = 0
    for i in range(num_cubes):
        side_length = float(input(f"Enter the side length of cube {i + 1}: "))
        cube_vol = cube_volume(side_length)
        total_volume += cube_vol

    print(f"\nThe total volume of all cubes is: {total_volume}")

if __name__ == "__main__":
    main()