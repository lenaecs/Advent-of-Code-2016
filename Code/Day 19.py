from collections import deque
import itertools


def gift_exchange(participants):
    part_list = range(1, participants + 1)
    part_list = deque(part_list)
    while len(part_list) > 1:
        del part_list[1]
        first_elf = part_list.popleft()
        part_list.append(first_elf)
    return part_list

#print(gift_exchange(5))
#print(gift_exchange(3014387))


def gift_exchange2(participants):
    part_list = range(1, participants + 1)
    part_list = part_list
    while len(part_list) > 1:
        to_del = len(part_list) / 2
        del part_list[to_del]
        first_elf = part_list.pop(0)
        part_list.append(first_elf)
        if len(part_list) % 10000 == 0:
            print float(participants - len(part_list)) / participants
    return part_list

print(gift_exchange2(5))
print(gift_exchange2(3014387))
