from typing import List

def main():
    data = []
    for line in open("real-input.txt").readlines():
        data.append([int(x) for x in line.strip().split()])
    
    safeLineCounter = 0
    
    for line in data:
        print(f"line {line}")
        is_safe = is_line_safe(line)
        if not is_safe:
            for i in range(len(line)):
                line_copy = line.copy()
                line_copy.pop(i)
                is_safe = is_line_safe(line_copy)
                if is_safe:
                    break

        if is_safe:
            safeLineCounter += 1
    
    print(f"Number of safe reports are {safeLineCounter}")

def is_line_safe(line: List[int]):
    correctFormat = True
    is_ascending = True
    is_descending = True

    for i in range(len(line) -1):

        current, next_value = line[i], line[i+1]

        # Check for consistent direction
        if current < next_value:
            is_descending = False
        elif current > next_value:
            is_ascending = False

        # Check for large jumps
        diff = abs(next_value - current)
        if diff < 1 or diff > 3:
            correctFormat = False
            break  # Exit early if a large jump is found

        if not is_ascending and not is_descending:
            correctFormat = False
            break
    
    return correctFormat

if __name__ == "__main__":
    main()