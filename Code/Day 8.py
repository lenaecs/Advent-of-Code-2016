f = open('C:\\Users\lenae.stoner\Dropbox\Advent-of-Code-2016\Input\Day 8.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']

def create_grid(width, height):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        grid.append(row)
    return grid

def two_factor(width, height, instr):
    grid = create_grid(width, height)
    for item in instr:
        if item[0:5] == 'rect ':
            item = item.replace('x', ' ')
            item = item.split()
            for i in range(int(item[1])):
                for j in range(int(item[2])):
                    grid[j][i] = 1
        if item[0:16] == 'rotate column x=':
            item = item.replace('=', ' ')
            item = item.split()
            column = []
            new_column = [0] * height
            for row in grid:
                column.append(row[int(item[3])])
            for position in range(len(column)):
                new_position = (position + int(item[5])) % height
                if column[position] == 1:
                    new_column[new_position] = 1
            for row in range(len(grid)):
                grid[row][int(item[3])] = new_column[row]
        if item[0:13] == 'rotate row y=':
            item = item.replace('=', ' ')
            item = item.split()
            new_row = [0] * width
            row = int(item[3])
            for position in range(len(grid[row])):
                new_position = (position + int(item[5])) % width
                if grid[row][position] == 1:
                    new_row[new_position] = 1
            grid[row] = new_row
    pixel_count = 0
    for row in grid:
        pixel_count += sum(row)
        line = ''
        for col in row:
            if col == 1:
                line += '#'
            else:
                line += ' '
        print line
    return pixel_count

print two_factor(7, 3, test)
print two_factor(50, 6, puzzle)