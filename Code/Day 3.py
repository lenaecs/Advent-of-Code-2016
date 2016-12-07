f = open('/Users/cye/Downloads/Day 3 Input.txt')

puzzle = []

for line in f:
    line = line.split()
    for i in [0,1,2]:
        line[i] = int(line[i])
    puzzle.append(line)

puzzle2 = []
tri0 = []
tri1 = []
tri2 = []

for line in puzzle:
    tri0.append(line[0])
    tri1.append(line[1])
    tri2.append(line[2])
    if len(tri0) == 3:
        puzzle2.append(list(tri0))
        puzzle2.append(list(tri1))
        puzzle2.append(list(tri2))
        tri0 = []
        tri1 = []
        tri2 = []

def check_triangle(triangle_list):
    possible = 0
    for triangle in triangle_list:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            possible += 1
    return possible

print check_triangle(puzzle)
print check_triangle(puzzle2)