f = open('/Users/cye/Downloads/Day 2 Input.txt')

puzzle = []

for line in f:
    puzzle.append(line)

test = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

keypad = [[1,2,3],[4,5,6],[7,8,9]]
keypad = [[1],[2,3,4],[5,6,7,8,9],['A','B','C'],['D']]

def keypad_ext(keypad):
    first_row = []
    last_row = []
    max_row_len = 0
    for row in keypad:
        if len(row) > max_row_len:
            max_row_len = len(row)
    for i in range(max_row_len):
        first_row.append(0)
    for i in range(max_row_len):
        last_row.append(0)
    keypad.insert(0, first_row)
    keypad.append(last_row)
    for row in keypad:
        while len(row) != max_row_len:
            row.insert(0, 0)
            row.append(0)
        row.insert(0,0)
        row.append(0)
    return keypad

print keypad_ext(keypad)

def bathroom_code(inst, keypad):
    keypad = keypad_ext(keypad)
    code = []
    for row in range(len(keypad)):
        if 5 in keypad[row]:
            key = [row, keypad[row].index(5)]
    for line in inst:
        for direct in line:
            if direct == 'U' and keypad[key[0] - 1][key[1]] != 0:
                key[0] -= 1
            if direct == 'D' and keypad[key[0] + 1][key[1]] != 0:
                key[0] += 1
            if direct == 'L' and keypad[key[0]][key[1] - 1] != 0:
                key[1] -= 1
            if direct == 'R' and keypad[key[0]][key[1] + 1] != 0:
                key[1] += 1
        code.append(keypad[key[0]][key[1]])
    print code

bathroom_code(test, keypad)
bathroom_code(puzzle, keypad)
