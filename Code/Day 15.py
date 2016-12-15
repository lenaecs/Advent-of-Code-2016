f = open('C:\Users\lenae.stoner\Dropbox\Advent-of-Code-2016\Input\Day 15.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.']

puzzle.append('Disc #7 has 11 positions; at time=0, it is at position 11.')

def machine_timer(disks):
    pos_dict = {}
    through_disks = False
    time = -1
    for disk in disks:
        disk = disk.split()
        pos_dict[int(disk[1][1])] = {'num_positions': int(disk[3]), 'start_pos' : int(disk[11].strip('.'))}
    while through_disks == False:
        time += 1
        through_disks = True
        for disk in range(1, len(pos_dict) + 1):
            pos_dict[disk]['current_pos'] = ((pos_dict[disk]['start_pos'] + time + disk) %
                                             pos_dict[disk]['num_positions'])
            if pos_dict[disk]['current_pos'] != 0:
                through_disks = False
    return time

print(machine_timer(test))
print(machine_timer(puzzle))