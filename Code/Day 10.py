f = open('C:\Users\lenae\Dropbox\Advent-of-Code-2016\Input\Day 10.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['value 5 goes to bot 2', 'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1', 'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0', 'value 2 goes to bot 2']

def balancer(instructions, output1, output2):
    bot_dict = {}
    output_dict = {}
    while instructions != []:
        items_to_drop = []
        for i in range(len(instructions)):
            instr = instructions[i].split()
            if instr[0] == 'value':
                if instr[5] in bot_dict:
                    bot_dict[instr[5]].append(int(instr[1]))
                else:
                    bot_dict[instr[5]] = [int(instr[1])]
                items_to_drop.append(i)
            if instr[0] == 'bot':
                if instr[1] in bot_dict and len(bot_dict[instr[1]]) == 2:
                    low = min(bot_dict[instr[1]])
                    high = max(bot_dict[instr[1]])
                    if instr[5] == 'output':
                        output_dict[instr[6]] = low
                    elif instr[5] == 'bot':
                        if instr[6] in bot_dict:
                            bot_dict[instr[6]].append(low)
                        else:
                            bot_dict[instr[6]] = [low]
                    if instr[10] == 'output':
                        output_dict[instr[11]] = high
                    elif instr[10] == 'bot':
                        if instr[11] in bot_dict:
                            bot_dict[instr[11]].append(high)
                        else:
                            bot_dict[instr[11]] = [high]
                    items_to_drop.append(i)
        for index in sorted(items_to_drop, reverse = True):
            del instructions[index]
    print(output_dict['1'] * output_dict['2'] * output_dict['0'])
    for bot in bot_dict:
        if output1 in bot_dict[bot] and output2 in bot_dict[bot]:
            return bot

#print(balancer(test, '5', '2'))
print(balancer(puzzle, 61, 17))

# First guess: 83-too low

# First guess: 8103 - too low