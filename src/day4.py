f = open("../inputs/day4.txt", "r")

lines = f.read().split("\n")

nums = list(map(int, lines[0].split(",")))
boards = []

for i in range(2, len(lines)-4, 6):
    board = []
    for j in range(5):
        board.append(list(int(s) for s in lines[i+j].split()))
    boards.append(board)

def find1():
    global boards
    drawn = set()
    for n in nums:
        drawn.add(n)
        for board in boards:
            good = False
            for i in range(5):
                if all(board[i][j] in drawn for j in range(5)):
                    good = True

            for j in range(5):
                if all(board[i][j] in drawn for i in range(5)):
                    good = True

            # if all(board[i][i] in drawn for i in range(5)):
            #     good = True
            #
            # if all(board[i][4-i] in drawn for i in range(5)):
            #     good = True

            if good:
                # print(n, board)
                s = 0
                for i in range(5):
                    for j in range(5):
                        if board[i][j] not in drawn:
                            s += board[i][j]
                return s * n

    return None

def find2():
    global boards
    drawn = set()
    for n in nums:
        drawn.add(n)
        temp = []
        for board in boards:
            good = False
            for i in range(5):
                if all(board[i][j] in drawn for j in range(5)):
                    good = True

            for j in range(5):
                if all(board[i][j] in drawn for i in range(5)):
                    good = True

            # if all(board[i][i] in drawn for i in range(5)):
            #     good = True
            #
            # if all(board[i][4-i] in drawn for i in range(5)):
            #     good = True

            if not good:
                # print(board, n)
                temp.append(board)
        boards = temp
        if len(boards) == 0 and len(temp) == 0:
            # print(n, board)
            s = 0
            for i in range(5):
                for j in range(5):
                    if board[i][j] not in drawn:
                        s += board[i][j]
            return s * n

    return None

print("part 1:", find1())
print("part 2:", find2())