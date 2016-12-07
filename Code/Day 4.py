import string

letter_count = []
for i in range(26):
    letter_count.append(i)

letter_number = dict(zip(string.ascii_lowercase, letter_count))
number_letter = dict(zip(letter_count, string.ascii_lowercase))

f = open('/Users/cye/Downloads/Day 4 Input.txt')

puzzle = []

for line in f:
    puzzle.append(line.rstrip())

test = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]']

alphebet_dict = {1:'a'}

def check_code(room_list):
    sector_sums = 0
    for room in room_list:
        sector = ''
        code = ''
        code_with_dash = ''
        for char in range(len(room)):
            if room[char] == '-':
                code_with_dash += room[char]
            elif room[char].isdigit():
                sector += room[char]
            elif room[char] == '[':
                start_check = char
                break
            else:
                code += room[char]
                code_with_dash += room[char]
        check_sum = room[start_check + 1:len(room) - 1]
        check_list = {}
        for letter in code:
            if letter in check_list:
                check_list[letter] += 1
            else:
                check_list[letter] = 1
        answer = ''
        while len(answer) < 5:
            max_count = max(check_list.values())
            to_add_to_answer = ''
            for key in check_list:
                if check_list[key] == max_count:
                    to_add_to_answer += key
            for item in to_add_to_answer:
                del check_list[item]
            answer = answer + ''.join(sorted(to_add_to_answer))
        if answer[0:5] == check_sum:
            room_name = ''
            for char in code_with_dash:
                if char == '-':
                   room_name += ' '
                else:
                    char_num = letter_number[char]
                    char_num += int(sector)
                    char_num = char_num%26
                    room_name += number_letter[char_num]
            if 'north' in room_name:
                print sector
    return sector_sums

print check_code(test)
print check_code(puzzle)

#first guess 188171, Too high