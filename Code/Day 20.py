import numpy

f = open('C:\Users\lenae\Dropbox\Advent-of-Code-2016\Input\Day 20.txt')

puzzle = []
for line in f:
    puzzle.append(line.strip())

test = ['5-8', '0-2', '4-7']

def firewall(banned, ran):
    possible_ips = set(xrange(ran + 1))
    for ip in banned:
        ip = ip.split('-')
        for value in range(int(ip[0]), int(ip[1]) + 1):
            if value in possible_ips:
                possible_ips.remove(value)
    return min(possible_ips)

print firewall(test, 9)

def firewall_big(banned, ran):
    cur_min = -1
    new_min = 0
    while cur_min != new_min:
        cur_min = new_min
        for ip in banned:
            ip = ip.split('-')
            if new_min >= numpy.uint32(ip[0]) and new_min <= numpy.uint32(ip[1]):
                new_min = 1 + numpy.uint32(ip[1])
    return new_min

print firewall_big(test, 9)
print firewall_big(puzzle, 4294967295)

def blacklist(banned, ran):
    banned_list = [[None, None]]
    for i in banned[1:]:
        i = i.split('-')
        i[0] = numpy.uint32(i[0])
        i[1] = numpy.uint32(i[1])
        for j in range(len(banned_list)):
            if i[0] <= banned_list[j][0] or j == len(banned_list)-1:
                banned_list.insert(j, i)
                break
    banned_list.pop() #gets rid of the [None, None]
    finished = False
    while finished == False:
        for ip in range(1, len(banned_list)):
            if banned_list[ip - 1][1] >= banned_list[ip][0] - 1:
                if banned_list[ip - 1][1] <= banned_list[ip][1]:
                    banned_list[ip - 1][1] = banned_list[ip][1]
                    del banned_list[ip]
                    break
                else:
                    del banned_list[ip]
                    break
            if ip == len(banned_list) - 1:
                finished = True
    banned_count = 0
    for ip in banned_list:
        banned_count += ip[1] - ip[0] + 1
    return ran - banned_count +1

print blacklist(test, 9)
print blacklist(puzzle, 4294967295)

#first guess: 3529252405 too high
#second guess: 765714890 too high
#third guess: 124 too low
