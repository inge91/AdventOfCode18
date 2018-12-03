def uniqueLetterFrequencies(word):
    frequencies = []
    history = []
    for i in range(0, len(word)):
        referenceLetter = word[i]
        count = 1
        if referenceLetter in history:
            continue
        history.append(referenceLetter)
        for j in range(i + 1, len(word)):
            if word[j] == referenceLetter:
                count += 1
        frequencies.append(count)
    return frequencies

def part1(boxes):
    boxWithThreeRepeated = 0
    boxWithTwoRepeated = 0
    for box in boxes:
        counts = uniqueLetterFrequencies(box)
        if 3 in counts:
            boxWithThreeRepeated += 1
        if 2 in counts:
            boxWithTwoRepeated += 1
    print(boxWithTwoRepeated * boxWithThreeRepeated)

def getSimilarityString(word1, word2):
    similarityString = ""
    for i in range(0, len(word1)):
        if word1[i] == word2[i]:
            similarityString += word1[i]
    return similarityString

def part2(boxes):
    for i in range(0, len(boxes)):
        for j in range(i, len(boxes)):
            similarityString = getSimilarityString(boxes[i], boxes[j])
            if len(similarityString) == len(boxes[i]) - 1:
                print(similarityString)
                return

if __name__ == "__main__":
    f = open("input.txt", 'r')
    boxes = f.readlines();
    print("Part 1:")
    part1(boxes)
    print("Part 2:")
    part2(boxes)
