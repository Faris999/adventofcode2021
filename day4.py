# input handling

with open('day4input.txt', 'r') as f:
    draws = list(map(int, f.readline().split(',')))

    boards = []
    next_line = f.readline()
    while next_line:
        board = []
        for i in range(5):
            row = list(map(int, f.readline().split()))
            board.append(row)
        boards.append(board)
        next_line = f.readline()

def check_win(board):
    board = marked[board]
    for i in range(5):
        if all(board[i]):
            return True
    for i in range(5):
        if all(board[j][i] for j in range(5)):
            return True
    return False

# marked array
marked = [[[False for i in range(5)] for j in range(5)] for k in range(len(boards))]

# traverse the board based on the draws
for draw in draws:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, col in enumerate(row):
                if col == draw:
                    marked[i][j][k] = True
    
    # check if one of them wins
    for i, board in enumerate(boards):
        if check_win(i):
            print(i)
            print(board)
            break
    else:
        continue
    break

# calculate score
score = 0
winning_board = boards[i]
winning_marked = marked[i]
for i, row in enumerate(winning_board):
    for j, col in enumerate(row):
        if not winning_marked[i][j]:
            score += col
score *= draw
print(score)

# part 2
for draw in draws:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, col in enumerate(row):
                if col == draw:
                    marked[i][j][k] = True
    
    # check if one of them wins
    for i, board in enumerate(boards):
        if check_win(i):
            if len(boards) == 1:
                print(board)
                break
            del boards[i]
            del marked[i]
    else:
        continue
    break

# calculate score
score = 0
winning_board = boards[i]
winning_marked = marked[i]
for i, row in enumerate(winning_board):
    for j, col in enumerate(row):
        if not winning_marked[i][j]:
            score += col
score *= draw
print(score)
