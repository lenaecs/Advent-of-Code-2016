f = open('C:\Users\lenae.stoner\Dropbox\Advent-of-Code-2016\Input\Day 12.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']

def monorail(codes):
    register = {'a':0, 'b':0, 'c':1, 'd':0}
    instr = 0
    while instr < len(codes):
        code = codes[instr].split()
        if code[0] == 'cpy':
            if code[1].isdigit():
                register[code[2]] = int(code[1])
            else:
                register[code[2]] = register[code[1]]
            instr += 1
        elif code[0] == 'inc':
            register[code[1]] += 1
            instr += 1
        elif code[0] == 'dec':
            register[code[1]] -= 1
            instr += 1
        elif code[0] == 'jnz':
            if code[1].isdigit() and code[1] != '0':
                instr += int(code[2])
            elif register[code[1]] != 0:
                instr += int(code[2])
            else:
                instr += 1
    return register

#print(monorail(test))
print(monorail(puzzle))

#guess 1: 42, too low