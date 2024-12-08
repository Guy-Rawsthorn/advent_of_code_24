import re

def main():
    data = open("test-input.txt").read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    total = 0
    for match in matches:
        mul = int(match[0]) * int(match[1])
        total += mul
    
    print(f"total {total}")

    

if __name__ == "__main__":
    main()