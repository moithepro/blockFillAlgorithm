ROAD_BLOCK = 1
EMPTY = 0
START = 2


def readfile(filename):
    filearr = []
    with open(filename) as file:
        for line in file:
            filearr.append(line.strip().split())
    filearr2 = []
    for line in filearr:
        row = []
        for val in line:
            row.append(int(val))
        filearr2.append(row)
    return filearr2


def printarr(arr):
    for row in arr:
        for num in row:
            if num == EMPTY:
                # Print 0s in the default color (no color change)
                print(f"{num}", end="  ")
            elif num == ROAD_BLOCK:
                # Print 1s in red
                print(f"\033[31m{num}\033[0m", end="  ")
            elif num == START:
                # Print 2s in green
                print(f"\033[32m{num}\033[0m", end="  ")
            else:
                # Print other numbers in blue
                print(f"\033[34m{num}\033[0m", end="  ")
        print()  # Move to the next row


def printarr_with_arrows(arr, path):
    arrow_symbols = {
        (-2, 0): '↑',  # Up
        (2, 0): '↓',  # Down
        (0, -2): '←',  # Left
        (0, 2): '→',  # Right
        (-1, -1): '↖',  # Up-Left (Diagonal)
        (-1, 1): '↗',  # Up-Right (Diagonal)
        (1, -1): '↙',  # Down-Left (Diagonal)
        (1, 1): '↘',  # Down-Right (Diagonal)
    }

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            num = arr[row][col]

            if num == EMPTY:
                # Print 0s in the default color (no color change)
                print(f"{num}", end="  ")
            elif num == ROAD_BLOCK:
                # Print 1s in red
                print(f"\033[31m{num}\033[0m", end="  ")
            elif num == START:
                # Print 2s in green
                print(f"\033[32m{num}\033[0m", end="  ")
            else:
                # Print arrows in blue if this point is part of the path
                if (row, col) in path:
                    point_index = path.index((row, col))
                    if point_index < len(path) - 1:
                        # Get the next point in the path
                        next_row, next_col = path[point_index + 1]
                        # Get the last point in the path
                        last_row, last_col = path[point_index - 1]
                        # Calculate the direction
                        direction = ((next_row - row) - (last_row - row), (next_col - col) - (last_col - col))
                        # Get the corresponding arrow symbol
                        arrow = arrow_symbols.get(direction, '?')
                        # Print the arrow in blue
                        print(f"\033[34m{arrow}\033[0m", end="  ")
                    else:
                        # Last point in the path
                        print(f"\033[34m{'*'}\033[0m", end="  ")
                else:
                    # If it's not part of the path, just print the number
                    print(f"{num}", end="  ")
        print()
