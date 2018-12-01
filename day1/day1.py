def part1(numbers):
    frequency = 0;
    for number in numbers:
        frequency += number
    print(frequency)

def part2(numbers):
    frequency = 0;
    from sets import Set
    history = Set([0])
    historyRepeated = False
    while not historyRepeated:
        for number in numbers:
            frequency += number
            if frequency in history:
                historyRepeated = True
                break
            else:
                history.add(frequency)
    print(frequency)

def main():
    f =  open("day1.txt", 'r')
    lines = f.readlines()
    numbers = []
    for line in lines:
        if line[0] == "+":
            number = int(line[1:])
        else:
            number = int(line)
        numbers.append(number)
    print("Part 1:"),
    part1(numbers)
    print("Part 2:"),
    part2(numbers)


if __name__ == "__main__":
    main()



