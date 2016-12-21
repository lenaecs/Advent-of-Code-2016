import itertools

f = open('C:\Users\lenae.stoner\Dropbox\Advent-of-Code-2016\Input\Day 21.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['swap position 4 with position 0', 'swap letter d with letter b', 'reverse positions 0 through 4',
        'rotate left 1 step', 'move position 1 to position 4', 'move position 3 to position 0',
        'rotate based on position of letter b', 'rotate based on position of letter d']

def scramble(instr, password):
    password_list = []
    for letter in password:
        password_list.append(letter)
    for inst in instr:
        inst = inst.split()
        if inst[0] == 'swap':
            if inst[1] == 'position':
                a = password_list[int(inst[2])]
                b = password_list[int(inst[5])]
                password_list[int(inst[2])] = b
                password_list[int(inst[5])] = a
            elif inst[1] == 'letter':
                a = password_list.index(inst[2])
                b = password_list.index(inst[5])
                password_list[a] = inst[5]
                password_list[b] = inst[2]
        if inst[0] == 'reverse':
            new_list = password_list[int(inst[2]):int(inst[4]) + 1]
            new_list.reverse()
            password_list[int(inst[2]):int(inst[4]) + 1] = new_list
        if inst[0] == 'rotate':
            new_dict = {}
            if inst[1] == 'left':
                for pos in range(len(password_list)):
                    new_dict[(pos - int(inst[2])) % len(password_list)] = password_list[pos]
                password_list = []
                for pos in range(len(new_dict)):
                    password_list.append(new_dict[pos])
            if inst[1] == 'right':
                for pos in range(len(password_list)):
                    new_dict[(pos + int(inst[2])) % len(password_list)] = password_list[pos]
                password_list = []
                for pos in range(len(new_dict)):
                    password_list.append(new_dict[pos])
            if inst[1] == 'based':
                ind = password_list.index(inst[6])
                if ind >= 4:
                    rotate = ind + 2
                else:
                    rotate = ind + 1
                for pos in range(len(password_list)):
                    new_dict[(pos + rotate) % len(password_list)] = password_list[pos]
                password_list = []
                for pos in range(len(new_dict)):
                    password_list.append(new_dict[pos])
        if inst[0] == 'move':
            letter = password_list.pop(int(inst[2]))
            password_list.insert(int(inst[5]), letter)
        new_string = ''
        for letter in password_list:
            new_string +=(letter)
    return new_string

print scramble(test, 'abcde')
print scramble(puzzle, 'abcdefgh')


def reverse_password(string, password):
    all_permutations = itertools.permutations(string)
    for permutation in all_permutations:
        new_string = ''
        for letter in permutation:
            new_string += letter
        new_password = scramble(puzzle, new_string)
        if new_password == password:
            break
    return new_string

print reverse_password('abcdefgh', 'fbgdceah')
