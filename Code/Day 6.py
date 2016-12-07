f = open('C:\Users\lenae.stoner\Dropbox\Advent of Code\December 2016\Input\Day 6.txt')
puzzle =[]

for line in f:
    puzzle.append(line.strip())

test = ['eedadn','drvtee','eandsr','raavrd','atevrs','tsrnev','sdttsa','rasrtv','nssdts','ntnada','svetve','tesnvt',
        'vntsnd','vrdear','dvrsen','enarar']

def code_breaking(code):
    bookkeeping = []
    for i in code[0]:
        bookkeeping.append({})
    for line in code:
        for pos in range(len(line)):
            if line[pos] in bookkeeping[pos]:
                bookkeeping[pos][line[pos]] += 1
            else:
                bookkeeping[pos][line[pos]] = 1
    message = ''
    second_message = ''
    for item in bookkeeping:
        max_value =  max(item.values())
        min_value = min(item.values())
        for key in item:
            if item[key] == max_value:
                message += key
            elif item[key] == min_value:
                second_message += key
    return message, second_message

print code_breaking(test)
print code_breaking(puzzle)