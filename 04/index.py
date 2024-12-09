import re

count = 0
part2_count = 0

def main():
    grid = read_file_to_dict("real-input.txt")
    for row, values in grid.items():
        print(row)
        print(values)
        for list_index, item in enumerate(values):
            if item == "X":
                
                print(f"found X at {list_index}")
                check_horizontal(row, values, list_index, direction="right")
                check_horizontal(row, values, list_index, direction="left")
                
                check_vertical(grid, row, values, list_index, direction="down")
                check_vertical(grid, row, values, list_index, direction="up")

                check_diagonal(grid, row, values, list_index, direction="se")
                check_diagonal(grid, row, values, list_index, direction="sw")
                check_diagonal(grid, row, values, list_index, direction="ne")
                check_diagonal(grid, row, values, list_index, direction="nw")
            
            if item == "A":
                print(f"found A at {list_index}")
                check_part_2(grid, row, values, list_index)

    global count
    print(f"final count {count}")
    global part2_count
    print(f"part 2 count {part2_count}")

def check_part_2(grid, row, values, list_index):
    if list_index < 1: # Don't include index 0
        print("Too far left")
        return False
    elif list_index == len(values) -1: # Don't include last index
        print("Too far right")
        return False
    elif row < 1: # Don't include the first row
        print("too high")
        return False
    elif row == max(grid.keys()): # Don't include the last row
        print("too low")
        return False
    
    se_counter = Counter(direction="se")
    sw_counter = Counter(direction="sw")
    ne_counter = Counter(direction="ne")
    nw_counter = Counter(direction="nw")

    se = grid[row + se_counter.adjust()[1]][list_index + se_counter.x_value]
    sw = grid[row + sw_counter.adjust()[1]][list_index + sw_counter.x_value]
    ne = grid[row + ne_counter.adjust()[1]][list_index + ne_counter.x_value]
    nw = grid[row + nw_counter.adjust()[1]][list_index + nw_counter.x_value]
    
    a = (se, nw)
    print(a)
    b = (ne, sw)
    print(b)

    if a.count("M") ==1 and a.count("S")==1:
        if b.count("M") ==1 and b.count("S")==1:
            print(f"found valid PART2 X-MAS on row {row} starting at {list_index}")
            global part2_count
            part2_count += 1

def check_diagonal(grid, row, values, list_index, direction):
    print(f"analyzing {direction} diagonal {row}, {list_index}")

    # If we're going south east don't bother if your too far right or too low down.
    # 8 > (10 -3)
    # 7 > (9-3) = True | 6 > (9-3) = False
    if direction=="se":
        if list_index > len(values) - 4:
            print(f"{list_index} is great than {len(values)-4}")
            print("too far right")
            return False
        elif (row > max(grid.keys()) - 3):
            print("too low down")
            return False
    
    # If we're going south west don't bother if your too far left or too low down.
    # 4 < (4-1) = True
    # 7 > (9-3) = True | 6 > (9-3) = False
    if direction=="sw":
        if (list_index < 3):
            print(f"{list_index} is less than 3")
            print("too far left")
            return False
        elif (row > max(grid.keys()) - 3):
            print("too low down")
            return False
    
    # If we're going north east don't bother if too far right or too high.
    # 4 < (4-1) = True
    # 7 > (9-3) = True | 6 > (9-3) = False
    if direction=="ne":
        if (list_index > len(values) - 4):
            print(f"{list_index} is great than {len(values)-4}")
            print("too far right")
            return False
        elif (row < 3):
            print("too high")
            return False
    
    # If we're going north west don't bother if too far left or too high.
    # 4 < (4-1) = True
    # 7 > (9-3) = True | 6 > (9-3) = False
    if direction=="nw":
        if (list_index < 3):
            print(f"{list_index} is less than 3")
            print("too far left")
            return False
        elif row < 3:
            print("too high")
            return False
    
    counter = Counter(direction=direction)

    if grid[row + counter.adjust()[1]][list_index + counter.x_value] == "M":
        if grid[row + counter.adjust()[1]][list_index + counter.x_value] == "A":
            if grid[row + counter.adjust()[1]][list_index + counter.x_value] == "S":
                print(f"found valid {direction} diagonal XMAS on row {row} starting at {list_index}")
                global count
                count += 1

def check_vertical(grid, row, values, list_index, direction):
    print(f"analyzing {direction} vertical {row}, {list_index}")

    # if down but too low
    if direction=="down" and row > (max(grid.keys()) - 3):
        # print(f"down - {row} is too low")
        return False
    
    if direction=="up" and row < 3:
        # print(f"up - {row} is too high")
        return False
    
    counter = Counter(direction=direction)

    if grid[row + counter.adjust()[1]][list_index] == "M":
        if grid[row + counter.adjust()[1]][list_index] == "A":
            if grid[row + counter.adjust()[1]][list_index] == "S":
                print(f"found valid {direction} vertical XMAS on row {row} starting at {list_index}")
                global count
                count += 1

def check_horizontal(row, values, list_index, direction):
    print(f"analyzing {direction} horizonal {row}, {list_index}")
    
    counter = Counter(direction=direction)

    # if checking right but too far right
    if direction=="right" and list_index > len(values) - 4:
        return False
    # if checking left but too far left
    if direction=="left" and list_index < 3:
        return False

    if values[list_index + counter.adjust()[0]] == "M":
        if values[list_index + counter.adjust()[0]] == "A":
            if values[list_index + counter.adjust()[0]] == "S":
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
    def __init__(self, direction):
        self.x_value = 0
        self.y_value = 0
        self.direction = direction

    def adjust(self):
        if self.direction == "left":
            self.x_value -= 1
        elif self.direction == "right":
            self.x_value += 1
        elif self.direction == "down":
            self.y_value += 1
        elif self.direction == "up":
            self.y_value -= 1
        elif self.direction == "se":
            self.x_value += 1
            self.y_value += 1
        elif self.direction == "sw":
            self.x_value -= 1
            self.y_value += 1
        elif self.direction == "ne":
            self.x_value += 1
            self.y_value -= 1
        elif self.direction == "nw":
            self.x_value -= 1
            self.y_value -= 1
        return (self.x_value, self.y_value)


if __name__ == "__main__":
    main()