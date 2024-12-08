
import re

def main():
    data = open("real-input.txt").read()
    pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
    matches = re.finditer(pattern, data)
    ignore = False
    count = 0
    for i in matches:
        if "mul" in i[0] and not ignore:
            count += (int(i[1]) * int(i[2]))
        elif "don" in i[0]:
            ignore = True
        elif "do" in i[0]:
            ignore = False

    print(f"total {count}")    

if __name__ == "__main__":
    main()