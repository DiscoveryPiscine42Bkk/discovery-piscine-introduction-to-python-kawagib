def checkmate(board_str):

    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)

    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
            
    if king_pos is None:
        print("Error")
        return
    
    x, y = king_pos

    def is_enemy(i, j):
        return 0 <= i < size and 0 <= j < size
    
    for dx in [-1, 1]:
        i, j = x - 1, y + dx
        if is_enemy(i, j) and board[i][j] == 'P':
            print("Success")
            return
        
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = x + dx, y + dy
        while is_enemy(i, j):
            if board[i][j] != '.':
                if board[i][j] in ['R', 'Q']:
                    print("Seccess")
                    return
                break
            i += dx
            j += dy

    for dx, dy in [(-1, -1), (-1, 1), (-1, 1), (1, 1)]:
        i, j = x + dx, y + dy
        while is_enemy(i, j):
            if board[i][j] != '.':
                if board[i][j] in ['B', 'Q']:
                    print("Success")
                    return
                break
            i += dx
            j += dy

    print("Fail")