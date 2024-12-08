def main():
    data = []
    for line in open("test-input.txt").readlines():
        data.append([int(x) for x in line.strip().split()])
    
    correctFormatCounter = 0
    for line in data:
        
        correctFormat = True
        
        while correctFormat:
            if (is_descending(line) == False and is_accending(line) == False):
                correctFormat = False

            for i in range(len(line)-1):
                if abs(line[i+1] - line[i]) > 3:
                    correctFormat = False

            break

        if correctFormat == True:
            correctFormatCounter += 1
    
    print(f"Number of unsafe reports are {correctFormatCounter}")

def is_descending(line):
    for i in range(len(line) - 1):
        if line[i] <= line[i + 1]: # is right bigger or equal to then left
            return False
    return True

def is_accending(line):
    for i in range(len(line) - 1):
        if line[i] >= line[i + 1]: # is right smaller or equal to than left 
            return False
    return True


if __name__ == "__main__":
    main()