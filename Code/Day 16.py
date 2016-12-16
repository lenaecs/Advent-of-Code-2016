def generate_data(starting_str, length):
    output_str = starting_str
    while len(output_str) < length:
        str_copy = output_str
        str_copy = str_copy[::-1]
        part2 = ''
        for letter in str_copy:
            if letter == '0':
                part2 += '1'
            else:
                part2 += '0'
        output_str = output_str + '0' + part2
    return output_str[:length]

def checksum(starting_string):
    if len(starting_string) % 2 == 1:
        return starting_string
    else:
        new_string = ''
        for letter in range(0, len(starting_string), 2):
            if starting_string[letter] == starting_string[letter + 1]:
                new_string += '1'
            else:
                new_string += '0'
        return(checksum(new_string))


fake_data = generate_data('10000', 20)

print(checksum(fake_data))

fake_data = generate_data(('10011111011011001'), 272)
print(checksum(fake_data))

fake_data = generate_data(('10011111011011001'), 35651584)
print(checksum(fake_data))