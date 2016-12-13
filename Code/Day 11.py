# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

# The first floor contains a polonium generator, a thulium generator, a thulium-compatible
# microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip,
# a cobalt generator, and a cobalt-compatible microchip.
#
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.

test = [['hm', 'lm'], ['hg'], ['lg'], [], [0]]

puzzle = [['pg', 'tg', 'tm', 'og', 'rg', 'rm', 'cg', 'cm', 'eg', 'em', 'dg', 'dm'], ['pm', 'om'], [], [], [0]]

def score_state(board):
    score = 3 * len(board[3]) + 2 * len(board[2]) + 1 * len(board[1])
    return score

def legal_board_check(board):
    legal = True
    for floor in board[0:3]:
        m_list = []
        g_list = []
        for item in floor:
            if item[1] == 'm':
                m_list.append(item[0])
            else:
                g_list.append(item[0])
        for item in m_list:
            if item in g_list:
                pass
            elif g_list == []:
                pass
            else:
                legal = False
    return legal

def deep_copy(board):
    new_board = []
    for line in board:
        new_board.append(list(line))
    return new_board

def find_all_legal_moves(board):
    all_moves = []
    for floor in range(len(board) - 1):
        if floor == board[4][0]:
            for item in range(len(board[floor])):
                board_copy = deep_copy(board)
                mover = board_copy[floor].pop(item)
                if floor == 3:
                    board_copy[2].append(mover)
                    board_copy[4][0] = floor - 1
                    all_moves.append(board_copy)
                elif floor == 0:
                    board_copy[1].append(mover)
                    board_copy[4][0] = floor + 1
                    all_moves.append(board_copy)
                else:
                    board_copy2 = deep_copy(board_copy)
                    board_copy[floor + 1].append(mover)
                    board_copy[4][0] = floor + 1
                    board_copy2[floor - 1].append(mover)
                    board_copy2[4][0] = floor - 1
                    all_moves.append(board_copy)
                    all_moves.append(board_copy2)
            if len(board[floor]) >= 2 and floor != 3:
                for i in range(len(board[floor])):
                    for j in range(len(board[floor])):
                        if i > j:
                            board_copy = deep_copy(board)
                            mover1 = board_copy[floor].pop(i)
                            mover2 = board_copy[floor].pop(j)
                            board_copy[floor + 1].append(mover1)
                            board_copy[floor + 1].append(mover2)
                            board_copy[4][0] = floor + 1
                            all_moves.append(board_copy)
    all_legal_moves = []
    for move in all_moves:
        if legal_board_check(move) == True:
            if board[0] == []:
                if move[0] == []:
                    all_legal_moves.append(move)
            elif board[0] == [] and board[1] == []:
                if move[0] == [] and move[1] == []:
                    all_legal_moves.append(move)
            else:
                all_legal_moves.append(move)
    return all_legal_moves

def summarize_state(board):
    state = ''
    for floor in range(4):
        generators = 0
        chips = 0
        for item in board[floor]:
            if item[1] == 'g':
                generators += 1
            else:
                chips += 1
        state += str(floor) + str(generators) + str(chips)
    state += str(board[4][0])
    return state


def elevator(board):
    found_board = False
    moves_dict = {0:[board]}
    moves = 0
    seen_states = set([])
    state = summarize_state(board)
    seen_states.add(state)
    while found_board == False and moves < 100:
        new_board_set = []
        for board in moves_dict[moves]:
            new_boards = find_all_legal_moves(board)
            for new_board in new_boards:
                if new_board[0] == [] and new_board[1] == [] and new_board[2] == []:
                    found_board = True
                state = summarize_state(new_board)
                if state not in seen_states:
                    new_board_set.append(new_board)
                    seen_states.add(state)
        moves += 1
        moves_dict[moves] = new_board_set
    return moves


#print(elevator(test))
print(elevator(puzzle))

