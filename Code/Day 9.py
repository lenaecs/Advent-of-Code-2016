f = open('C:\\Users\lenae.stoner\Dropbox\Advent-of-Code-2016\Input\Day 9.txt')

puzzle = ''

for line in f:
    puzzle += line.strip()

test1 = 'ADVENT'
test2 = 'A(1x5)BC'
test3 = '(3x3)XYZ'
test4 = 'A(2x2)BCD(2x2)EFG'
test5 = '(6x1)(1x3)A'
test6 = 'X(8x2)(3x3)ABCY'

test7 = '(3x3)XYZ'
test8 = 'X(8x2)(3x3)ABCY'
test9 = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
test10 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

def decompressor(compressed):
    new_string = ''
    chars_needed = 0
    string_to_repeat = ''
    times_repeated = 0
    end_marker = 0
    for char in range(len(compressed)):
        if end_marker > 0:
            end_marker -= 1
        elif chars_needed > 0:
            chars_needed -= 1
            string_to_repeat += compressed[char]
            if chars_needed == 0:
                new_string += string_to_repeat * times_repeated
                string_to_repeat = ''
        elif chars_needed == 0:
            if compressed[char] == '(':
                end_marker = compressed[char:].index(')')
                marker = compressed[char + 1:char + end_marker]
                marker = marker.split('x')
                chars_needed = int(marker[0])
                times_repeated = int(marker[1])
            else:
                new_string += compressed[char]
    return len(new_string)

# print decompressor(test1)
# print decompressor(test2)
# print decompressor(test3)
# print decompressor(test4)
# print decompressor(test5)
# print decompressor(test6)
# print decompressor(puzzle)

def decompressor2(compressed):
    decomp_len = 0
    end_marker = 0
    for char in range(len(compressed)):
        if end_marker > 0:
            end_marker -= 1
        elif compressed[char] == '(':
            end_marker = compressed[char:].index(')')
            marker = compressed[char + 1:char + end_marker]
            marker = marker.split('x')
            decomp_len += (int(marker[1]) *
                          decompressor2(compressed[char + end_marker + 1:char + end_marker + int(marker[0]) + 1]))
            end_marker += int(marker[0])
        else:
            decomp_len += 1
    return decomp_len

print decompressor2(test7)
print decompressor2(test8)
print decompressor2(test9)
print decompressor2(test10)
print decompressor2(puzzle)