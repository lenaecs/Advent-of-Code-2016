def minesweep(input_str, length):
    safe_squares = 0
    current_string = '.' + input_str + '.'
    for char in input_str:
        if char == '.':
            safe_squares += 1
    for i in range(length - 1):
        new_string = ''
        for j in range(1, len(current_string) - 1):
            if current_string[j - 1] != current_string[j + 1]:
                new_string += '^'
            else:
                new_string += '.'
                safe_squares += 1
        current_string = '.' + new_string + '.'
    return safe_squares

print(minesweep('..^^.', 3))
print(minesweep('.^^.^.^^^^', 10))
print(minesweep('^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^',
                400000))