def main():
    num_cubes = int(input("Enter the number of cubes: "))

    total_volume = 0
    for i in range(num_cubes):
        dimensions = []
        dimension_count = 3

        while dimension_count > 0:
            side_length = float(input(f"Enter the side length of cube {i + 1} (dimension {4 - dimension_count}): "))
            dimensions.append(side_length)
            dimension_count -= 1

        cube_vol = cube_volume(dimensions)
        total_volume += cube_vol

    print(f"\nThe total volume of all cubes is: {total_volume}")

def cube_volume(dimensions):
    return dimensions[0] * dimensions[1] * dimensions[2]

if __name__ == "__main__":
    main()