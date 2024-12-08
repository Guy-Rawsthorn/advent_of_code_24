def main():
    data = []
    for line in open("test-input.txt").readlines():
        data.append([int(x) for x in line.strip().split()])
    
    correctFormatCounter = 0
    
    for line in data:
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

        print(f"line {line} is {correctFormat}")
        if correctFormat == True:
            correctFormatCounter += 1
    
    print(f"Number of safe reports are {correctFormatCounter}")

if __name__ == "__main__":
    main()