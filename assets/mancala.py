import numpy as np
import time

aMancalaIndex = 6
bMancalaIndex = 13
turnA = True

gameBoard = np.array([4] * 14)
gameBoard[aMancalaIndex] = 0
gameBoard[bMancalaIndex] = 0


def print_board(board):
    gap = (len(str('B mancala')) - len(str(board[13])) - 2) * ' '
    gap2 = (len(str('B mancala')) - len(str(board[6])) - 2) * ' '
    print((len(str(board[13]))) * ' ', gap + '  ', 'B6', 'B5', 'B4', 'B3', 'B2', 'B1')
    print(board[13], gap, board[12], board[11], board[10], board[9], board[8], board[7], "A Mancala", sep='  ')
    print('B Mancala', board[0], board[1], board[2], board[3], board[4], board[5], gap2, board[6], sep='  ')
    print((len(str('B mancala')) + 1) * ' ', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6')


def move(pick, board):
    global turnA
    # stopping condition for multimove bots
    if pick is None:
        return not turnA

    cur_mancala = 0
    opp_mancala = 0
    ind = 0
    if turnA:
        cur_mancala = aMancalaIndex
        opp_mancala = bMancalaIndex
        ind = pick - 1
    else:
        cur_mancala = bMancalaIndex
        opp_mancala = aMancalaIndex
        ind = pick + 6

    cnt = board[ind]
    board[ind] = 0
    while cnt != 0:
        ind += 1
        if ind == opp_mancala:
            ind += 1
        if ind == 14:
            ind = 0
        board[ind] += 1
        cnt -= 1
    if ind != cur_mancala:
        if board[ind] == 1 and cur_mancala - 6 <= ind < cur_mancala:
            board[cur_mancala] += board[12 - ind] + 1
            board[ind] = 0
            board[12 - ind] = 0
        return not turnA
    else:
        return turnA


def check_end(board):
    return sum(board[0:6]) == 0 or sum(board[7:13]) == 0


def get_move_player(board):
    while True:
        if turnA:
            m = input("Player A Turn: ").strip()
        else:
            m = input("Player B Turn: ").strip()

        if m.isdigit():
            i = int(m)
            if 1 <= i <= 6:
                if (turnA and board[i - 1] != 0) or (not turnA and board[i + 6] != 0):
                    return i
                print("Pick a space that is not empty")
                continue
        print("Please Input a value between 1 and 6")


def get_move_random(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]
    return np.random.choice(np.flatnonzero(l)) + 1


def get_move_biggest(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]
    return np.random.choice(np.flatnonzero(l == np.amax(l))) + 1


def get_move_smallest(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]
    return np.random.choice(np.flatnonzero(l == np.amin(l[l != 0]))) + 1


def get_move_median(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]
    if np.median(l[1:]) != 0:
        return np.random.choice(np.flatnonzero(l == round(np.median(l[1:])))) + 1
    else:
        return np.argmin(l[l != 0]) + 1


def get_move_highest(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]

    return np.flatnonzero(l)[-1] + 1


def get_move_lowest(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]
    # print(l)
    return np.flatnonzero(l)[0] + 1


def get_move_middle(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]

    return np.median(np.flatnonzero(l)) + 1


def longest_helper(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]

    moves = []
    for i, x in enumerate(l):
        # if (i + x) % 13 == 6 or i + x == 19 or i + x == 32:
        if (i + x) % 13 == 6:
            newboard = np.copy(board)
            move(i + 1, newboard)
            moves.append([i + 1] + longest_helper(newboard))
    if moves:
        return max(moves)
    else:
        return []


def get_move_longest(board):
    for m in longest_helper(board):
        move(m, board)
        # print_board(board)
    if check_end(board):
        return None
    else:
        return get_move_random(board)


def get_move_highest_score(board):
    l = []
    if turnA:
        l = board[0:6]
    else:
        l = board[7:13]

    scores = np.array([0] * 6)
    for i, x in enumerate(l):
        # if (i + x) % 13 == 6 or i + x == 19 or i + x == 32:
        if x == 0:
            continue
        newboard = np.copy(board)
        move(i + 1, newboard)
        if turnA:
            scores[i] = newboard[aMancalaIndex]
        else:
            scores[i] = newboard[bMancalaIndex]
    return np.argmax(scores) + 1


def highest_score_deep_helper(board):
    l = []
    cur_mancala = 0
    if turnA:
        l = board[0:6]
        cur_mancala = aMancalaIndex
    else:
        l = board[7:13]
        cur_mancala = bMancalaIndex

    if check_end(board):
        return [], board[cur_mancala]

    moves = []
    scores = np.array([0] * 6)
    for i, x in enumerate(l):
        newboard = np.copy(board)
        if move(i + 1, newboard) == turnA:
            mo, so = highest_score_deep_helper(newboard)
            moves.append([i + 1] + mo)
            scores[i] = so
        else:
            moves.append([i + 1])
            scores[i] = newboard[cur_mancala]
    # print(moves)
    # print(scores)
    ind = np.random.choice(np.flatnonzero(scores == np.amax(scores)))
    return moves[ind], scores[ind]


def get_move_highest_score_deep(board):
    # st = time.time()
    moves = highest_score_deep_helper(board)[0]
    for m in moves[:-1]:
        # if turnA:
        # print("Player A Turn: A" + str(m))
        # else:
        print("Player B Turn: B" + str(m))
        move(m, board)
        print_board(board)
    print("Player B Turn: B" + str(moves[-1]))
    move(moves[-1], board)
    # print("search time: " + str(time.time() - st))
    return None


def highest_score_deep_first_helper(board):
    l = []
    cur_mancala = 0
    if turnA:
        l = board[0:6]
        cur_mancala = aMancalaIndex
    else:
        l = board[7:13]
        cur_mancala = bMancalaIndex

    if check_end(board):
        return [], board[cur_mancala]

    moves = []
    scores = np.array([0] * 6)
    for i, x in enumerate(l):
        newboard = np.copy(board)
        if move(i + 1, newboard) == turnA:
            mo, so = highest_score_deep_first_helper(newboard)
            moves.append([i + 1] + mo)
            scores[i] = so
        else:
            moves.append([i + 1])
            scores[i] = newboard[cur_mancala]
    # print(moves)
    # print(scores)
    ind = np.argmax(scores)
    return moves[ind], scores[ind]


def get_move_highest_score_deep_first(board):
    # st = time.time()
    for m in highest_score_deep_first_helper(board)[0]:
        # if turnA:
        #    print("Player A Turn: A" + str(m))
        # else:
        #    print("Player B Turn: B" + str(m))
        move(m, board)
        # print_board(board)
    # print("search time: " + str(time.time() - st))
    return None


def test_branches(board):
    global turnA
    cnt = 1000000
    times = []

    def branchtest1(board):
        l = []
        if turnA:
            l = board[0:6]
        else:
            l = board[7:13]
        return l[0]

    def branchtest2(board):
        l = board[(1 - turnA) * 7: (1 - turnA) * 7 + 6]
        return l[0]

    def branchtest3(board):
        n = (1 - turnA) * 7
        l = board[n: n + 6]
        return l[0]

    st = time.time()
    for i in range(cnt):
        branchtest1(board)
        turnA = not turnA
    times.append(time.time() - st)

    st = time.time()
    for i in range(cnt):
        branchtest2(board)
        turnA = not turnA
    times.append(time.time() - st)

    st = time.time()
    for i in range(cnt):
        branchtest3(board)
        turnA = not turnA
    times.append(time.time() - st)
    print(times)


def wrap_up_game(board):
    print_board(board)
    print("Summing Leftover Pieces")
    board[6] += sum(board[0:6])
    board[13] += sum(board[7:13])
    for x in range(6):
        board[x] = 0
    for x in range(7, 13):
        board[x] = 0
    print_board(board)
    if board[aMancalaIndex] > board[bMancalaIndex]:
        print("Player A Wins!")
    elif board[aMancalaIndex] < board[bMancalaIndex]:
        print("Player B Wins!")
    else:
        print("It's a Tie!")


def reset_board(board):
    global turnA
    turnA = True

    for x in range(14):
        board[x] = 4

    board[aMancalaIndex] = 0
    board[bMancalaIndex] = 0


def wrap_up_no_print(board):
    board[6] += sum(board[0:6])
    board[13] += sum(board[7:13])
    if board[aMancalaIndex] > board[bMancalaIndex]:
        reset_board(board)
        return 'a'
    elif board[aMancalaIndex] < board[bMancalaIndex]:
        reset_board(board)
        return 'b'
    else:
        reset_board(board)
        return 't'


def run_round(af, bf, board):
    global turnA
    while not check_end(board):
        if turnA:
            # print(af)
            turnA = move(af(board), board)
        else:
            # print(bf)
            turnA = move(bf(board), board)
    return wrap_up_no_print(board)


def run_comp(board):
    funclist = [get_move_random, get_move_biggest, get_move_smallest, get_move_highest, get_move_lowest,
                get_move_longest, get_move_highest_score, get_move_highest_score_deep,
                get_move_highest_score_deep_first]
    wls = np.zeros((len(funclist), len(funclist), 2))
    rounds = 100
    for i, x in enumerate(funclist):
        for j, y in enumerate(funclist):
            for z in range(rounds):
                r = run_round(x, y, board)
                if r == 'a':
                    wls[i][j][0] += 1
                elif r == 'b':
                    wls[i][j][1] += 1
                else:
                    wls[i][j][0] += 1
                    wls[i][j][1] += 1

    wlratio = np.zeros((len(funclist), len(funclist)))
    for i, row in enumerate(wls):
        for j, col in enumerate(row):
            wlratio[i][j] = col[0] / (col[0] + col[1])

    for row in wlratio:
        print(row)
    np.savetxt('output.csv', wlratio, delimiter=",", fmt='%1.3f')


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    # run_comp(gameBoard)
while not check_end(gameBoard):
    print_board(gameBoard)
    if turnA:
        turnA = move(get_move_player(gameBoard), gameBoard)
    else:
        turnA = move(get_move_highest_score_deep(gameBoard), gameBoard)
wrap_up_game(gameBoard)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
