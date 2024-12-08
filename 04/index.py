import re

count = 0

def main():
    grid = read_file_to_dict("test-input.txt")
    for row, values in grid.items():
        print(row)
        print(values)
        for list_index, item in enumerate(values):
            if item == "X":
                print(f"found x at {list_index}")
                # check_horizontal(row, values, list_index, direction="right")
                # check_horizontal(row, values, list_index, direction="left")
                # check_vertical(grid, row, values, list_index, direction="down")
                # check_vertical(grid, row, values, list_index, direction="up")

                check_diagonal(grid, row, values, list_index, direction="se")
                # check_diagonal(grid, row, values, list_index, direction="sw")

    global count
    print(f"final count {count}")

def check_diagonal(grid, row, values, list_index, direction):
    print(f"analyzing {direction} diagonal {row}, {list_index}")

    # If we're going south east don't bother if your too far right or too low down.
    # 8 > (10 -3)
    # 7 > (9-3) = True | 6 > (9-3) = False
    if direction=="se" and (list_index > len(values) -len("XMAS") -1 or row > (max(grid.keys())) - 3): 
        return False
    
    counter = Counter()
    
    if grid[row + counter.adjust("se")][list_index + counter.value] == "M":
        if grid[row + counter.adjust("se")][list_index + counter.value] == "A":
            if grid[row + counter.adjust("se")][list_index + counter.value] == "S":
                print(f"found valid {direction} diagonal XMAS on row {row} starting at {list_index}")
                global count
                count += 1

def check_vertical(grid, row, values, list_index, direction):
    print(f"analyzing {direction} vertical {row}, {list_index}")

    # if down but last key
    if direction=="down" and row == max(grid.keys()):
        return False
    if direction=="up" and row == 0:
        return False
    
    counter = Counter()

    if grid[row + counter.adjust(direction)][list_index] == "M":
        if grid[row + counter.adjust(direction)][list_index] == "A":
            if grid[row + counter.adjust(direction)][list_index] == "S":
                print(f"found valid {direction} vertical XMAS on row {row} starting at {list_index}")
                global count
                count += 1

def check_horizontal(row, values, list_index, direction):
    print(f"analyzing {direction} horizonal {row}, {list_index}")
    
    counter = Counter()

    # if right but end of row
    if direction=="right" and list_index == len(values) -1:
        return False
    # if left but end of row
    if direction=="left" and list_index == 0:
        return False

    if values[list_index + counter.adjust(direction)] == "M":
        if values[list_index + counter.adjust(direction)] == "A":
            if values[list_index + counter.adjust(direction)] == "S":
                print(f"found valid {direction} horizontal XMAS on row {row} starting at {list_index}")
                global count
                count += 1

def read_file_to_dict(file_path: str):
    grid = {}
    with open(file_path, 'r') as file:
        for row_index, line in enumerate(file):
            grid[row_index] = list(line.strip())
    return grid

class Counter:
    def __init__(self):
        self.value = 0

    def adjust(self, direction):
        if direction == "left":
            self.value -= 1
        elif direction == "right":
            self.value += 1
        elif direction == "down":
            self.value += 1
        elif direction == "up":
            self.value -= 1
        elif direction == "se":
            self.value += 1
        return self.value


if __name__ == "__main__":
    main()