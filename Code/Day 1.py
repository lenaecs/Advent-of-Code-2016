advent = open('C:\Users\lenae\Dropbox\Advent of Code\December 2016\Input\Day 1.txt')

input = []
for line in advent:
    input = line



def navigate(dir):
    dir = dir.split(', ')
    loc = [0,0]
    orientation = 0
    visited = ['00']
    bunny = False
    for i in dir:
        if i[0] == 'L':
            orientation = (orientation + 1)%4
        else:
            orientation =  (orientation - 1)%4
        if orientation == 0:
            for i in range(int(i[1:])):
                loc[0] += 1
                visited.append(str(loc[0]) + str(loc[1]))
                if len(set(visited)) == len(visited) and bunny == False:
                    pass
                elif bunny == True:
                    pass
                elif len(set(visited)) != len(visited):
                    bunny = True
                    print "bunny at " + str(abs(loc[0]) + abs(loc[1]))
        elif orientation == 1:
            for i in range(int(i[1:])):
                loc[1] += 1
                visited.append(str(loc[0]) + str(loc[1]))
                if len(set(visited)) == len(visited) and bunny == False:
                    pass
                elif bunny == True:
                    pass
                elif len(set(visited)) != len(visited):
                    bunny = True
                    print "bunny at " + str(abs(loc[0]) + abs(loc[1]))
        elif orientation == 2:
            for i in range(int(i[1:])):
                loc[0] -= 1
                visited.append(str(loc[0]) + str(loc[1]))
                if len(set(visited)) == len(visited) and bunny == False:
                    pass
                elif bunny == True:
                    pass
                elif len(set(visited)) != len(visited):
                    bunny = True
                    print "bunny at " + str(abs(loc[0]) + abs(loc[1]))
        else:
            for i in range(int(i[1:])):
                loc[1] -= 1
                visited.append(str(loc[0]) + str(loc[1]))
                if len(set(visited)) == len(visited) and bunny == False:
                    pass
                elif bunny == True:
                    pass
                elif len(set(visited)) != len(visited):
                    bunny = True
                    print "bunny at " + str(abs(loc[0]) + abs(loc[1]))
    print abs(loc[0]) + abs(loc[1])

navigate('R2, L3')
navigate('R2, R2, R2')
navigate('R5, L5, R5, R3')
navigate('R8, R4, R4, R8')
navigate(input)