from typing import List
from collections import Counter

def main():
    lists = extract_data("real-input.txt")
    left = lists[0]
    right = lists[1]
    left.sort()
    right.sort()
    distance = []
    for i in range(len(left)):
        distance.append(abs(left[i] - right[i]))
    
    print(f"The Total distance is {sum(distance)}")
    rightCounter = Counter(right)
    count = 0
    for val in left:
        score = rightCounter.get(val, 0)
        count += val * score

    print(f"Counter List {count}")
        

def extract_data(file_name: str) -> tuple[List[int], List[int]]:
    distance_file = open(file_name)
    lines = distance_file.readlines()
    left = []
    right = []
    for line in lines:
        numbers = line.strip().split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    return (left,right)


if __name__ == "__main__":
    main()