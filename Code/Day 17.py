import hashlib

def grid_navigation(starting_code):
    location = (0, 0)
    hashable = starting_code
    visited_dict = {0:[('', location)]}
    visited = 0
    location_found = False
    while location_found == False:
        new_states = []
        for state in visited_dict[visited]:
            md5_hash = hashlib.md5()
            md5_hash.update((hashable + state[0]))
            hashed = md5_hash.hexdigest()
            if hashed[0] in ('b', 'c', 'd', 'e', 'f') and state[1][0] > 0:
                new_loc = (state[1][0] - 1, state[1][1])
                new_states.append((state[0] + 'U', new_loc))
                if new_loc == (3, 3):
                    location_found = True
                    path = state[0] + 'U'
            if hashed[1] in ('b', 'c', 'd', 'e', 'f') and state[1][0] < 3:
                new_loc = (state[1][0] + 1, state[1][1])
                new_states.append((state[0] + 'D', new_loc))
                if new_loc == (3, 3):
                    location_found = True
                    path = state[0] + 'D'
            if hashed[2] in ('b', 'c', 'd', 'e', 'f') and state[1][1] > 0:
                new_loc = (state[1][0], state[1][1] - 1)
                new_states.append((state[0] + 'L', new_loc))
                if new_loc == (3, 3):
                    location_found = True
                    path = state[0] + 'L'
            if hashed[3] in ('b', 'c', 'd', 'e', 'f') and state[1][1] < 3:
                new_loc = (state[1][0], state[1][1] + 1)
                new_states.append((state[0] + 'R', new_loc))
                if new_loc == (3, 3):
                    location_found = True
                    path = state[0] + 'R'
        visited += 1
        visited_dict[visited] = new_states
    return path

print(grid_navigation('ihgpwlah'))
print(grid_navigation('kglvqrro'))
print(grid_navigation('ulqzkmiv'))
print(grid_navigation('awrkjxxr'))

def longest_path(starting_code):
    location = (0, 0)
    hashable = starting_code
    visited_dict = {0:[('', location)]}
    visited = 0
    new_states = set([1])
    while len(new_states) > 0:
        new_states = set([])
        for state in visited_dict[visited]:
            md5_hash = hashlib.md5()
            md5_hash.update((hashable + state[0]))
            hashed = md5_hash.hexdigest()
            if hashed[0] in ('b', 'c', 'd', 'e', 'f') and state[1][0] > 0:
                new_loc = (state[1][0] - 1, state[1][1])
                if new_loc == (3, 3):
                    longest_path = visited + 1
                else:
                    new_states.add((state[0] + 'U', new_loc))
            if hashed[1] in ('b', 'c', 'd', 'e', 'f') and state[1][0] < 3:
                new_loc = (state[1][0] + 1, state[1][1])
                if new_loc == (3, 3):
                    longest_path = visited + 1
                else:
                    new_states.add((state[0] + 'D', new_loc))
            if hashed[2] in ('b', 'c', 'd', 'e', 'f') and state[1][1] > 0:
                new_loc = (state[1][0], state[1][1] - 1)
                if new_loc == (3, 3):
                    longest_path = visited + 1
                else:
                    new_states.add((state[0] + 'L', new_loc))
            if hashed[3] in ('b', 'c', 'd', 'e', 'f') and state[1][1] < 3:
                new_loc = (state[1][0], state[1][1] + 1)
                if new_loc == (3, 3):
                    longest_path = visited + 1
                else:
                    new_states.add((state[0] + 'R', new_loc))
        visited += 1
        visited_dict[visited] = new_states
    return longest_path


print(longest_path('ihgpwlah'))
print(longest_path('kglvqrro'))
print(longest_path('ulqzkmiv'))
print(longest_path('awrkjxxr'))