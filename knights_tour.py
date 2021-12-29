import random

def knights_tour(board_size):
    board = [[0 for i in range(board_size)] for j in range(board_size)]
    moves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))

    def allowed_moves(position):
        allowed = []
        allowed_moves = set((position[0]+x, position[1]+y) for x,y in moves)
        allowed_moves = set((x,y) for x,y in allowed_moves if 0 <= x < board_size and 0 <= y < board_size)
        return allowed_moves

    def tour(position, board, counter):
        board[position[0]][position[1]] = counter
        if counter == board_size**2:
            for row in board:
                print(*row)
            return True
        moves = allowed_moves(position)
        #random.shuffle(moves)
        for move in moves:
            if not board[move[0]][move[1]]:
                if tour(move, board, counter+1):
                    return True
        else:
            board[position[0]][position[1]] = 0
            return False
        

    tour([0,0], board, 1)


knights_tour(8)
