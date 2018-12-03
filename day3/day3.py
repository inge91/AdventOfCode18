class Patch:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.x2 = x + w
        self.y2 = y + h

    def calculateArea(self):
        return (self.x2 - self.x) * (self.y2 - self.y)

    def calculateOverlapPatch(self, patch):
        if patch.x > self.x2 or self.x > patch.x2:
            return Patch(0,0,0,0)
        if patch.y > self.y2 or self.y > patch.y2:
            return Patch(0,0,0,0)
        minX = max(patch.x, self.x)
        minX2 = min(patch.x2, self.x2)
        minY = max(patch.y, self.y)
        minY2 = min(patch.y2, self.y2)
        return Patch(minX, minY, minX2 - minX, minY2 - minY)

def calculateNewOverlap(overlapPatch, fabric):
    overlap = 0
    for i in range(overlapPatch.x, overlapPatch.x2):
        for j in range(overlapPatch.y, overlapPatch.y2):
            if fabric[j][i] != 1:
                overlap += 1
                fabric[j][i] = 1
    return overlap

def part1(patches, fabric):
    overlap = 0
    for i in xrange(0, len(patches)):
        patch1 = patches[i]
        for j in xrange(i + 1, len(patches)):
            overlapPatch = patch1.calculateOverlapPatch(patches[j])
            overlap += calculateNewOverlap(overlapPatch, fabric)
    print(overlap)

def part2(patches, fabric):
    for i in range(0, len(patches)):
        patch = patches[i]
        if(calculateNewOverlap(patch, fabric) == patch.calculateArea()):
            print(i+1) # zero indexation

if __name__ == "__main__":
    f = open("input.txt", 'r')
    lines = f.readlines()
    patches = []
    maxWidth = 0
    maxHeight = 0
    for line in lines:
        splitLine = line.split(" ")
        x, y = splitLine[2][:-1].split(",")
        w, h = splitLine[3].split("x")
        p = Patch(int(x), int(y), int(w), int(h))
        patches.append(p)
        maxWidth = max(maxWidth, p.x2)
        maxHeight = max(maxHeight, p.y2)
    fabric = [[0 for x in range(0, maxWidth)] for x in range(0, maxHeight)]
    print("part 1")
    part1(patches, fabric)
    print("part 2")
    part2(patches, fabric)
