def open_space(x, y, number):
    if x < 0 or y < 0:
        return False
    else:
        equation = x*x + 3 * x + 2 * x * y + y + y * y
        add_number = equation + number
        binary_rep = bin(add_number)
        one_bits = 0
        for i in binary_rep[2:]:
            one_bits += int(i)
        if one_bits % 2 == 0:
            return True
        else:
            return False

def gen_all_valid_moves(x, y, number):
    moves = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    valid_moves = []
    for move in moves:
        if open_space(move[0], move[1], number) == True:
            valid_moves.append(move)
    return valid_moves

def maze_navigate(start_x, start_y, number, end_x, end_y):
    visited = set([(start_x, start_y)])
    steps = 0
    last_visited = [(start_x, start_y)]
    found = False
    while not found:
        steps += 1
        next_to_check = []
        for coord in last_visited:
            for move in gen_all_valid_moves(coord[0], coord[1], number):
                if move[0] == end_x and move[1] == end_y:
                    found = True
                if move not in visited:
                    visited.add(move)
                    next_to_check.append(move)
        last_visited = list(next_to_check)
    return steps

print(maze_navigate(1,1,10,7,4))
print(maze_navigate(1,1,1358,31,39))

def area_covered(start_x, start_y, number):
    visited = set([(start_x, start_y)])
    steps = 0
    last_visited = [(start_x, start_y)]
    while steps <= 49:
        steps += 1
        next_to_check = []
        for coord in last_visited:
            for move in gen_all_valid_moves(coord[0], coord[1], number):
                if move not in visited:
                    visited.add(move)
                    next_to_check.append(move)
        last_visited = list(next_to_check)
    return len(visited)

print area_covered(1,1,1358)

# guessed 143, too high