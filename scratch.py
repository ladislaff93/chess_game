board=[
        ["bR","bN","bB","bQ","bK","bB","bN","bR"],
        ["bP","bP","bP","bP","bP","bP","bP","bP"],
        ['--','--','--','--','--','--','--','--'],
        ['--','--','--','--','--','--','--','--'],
        ['--','--','--','--','--','--','--','--'],
        ['--','--','--','--','--','--','--','--'],            
        ["--","wP","wP","wP","wP","wP","wP","wP"],
        ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

moves = []
row = 7 
column = 1 
enemy = 'b'

def bishop_move(row, column, moves):
    direction = ((1,1),(-1,1),(1,-1),(-1,-1))
    for d in direction:
        for l in range(len(board)):
            r = l*d[0]
            c = l*d[1]      
            end_r = row + r 
            end_c = column + c 
            if 0 <= end_r <= 7 and 0 <= end_c <= 7:
                end_sq = board[end_r][end_c]
                if end_sq == '--' :
                    moves.append((board[end_r][end_c]))
                elif end_sq[0] == enemy:
                    moves.append((board[end_r][end_c]))
                    break

def rook_move(row, column, moves): #rook move logic. Rook can move in perpendicular way and for full lenght of the board (in cross.)
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    for d in direction:
        for l in range(len(board)):
            r = l*d[0]
            c = l*d[1]      
            end_r = row + r 
            end_c = column + c 
            if 0 <= end_r <=7 and 0 <= end_c <=7:
                end_sq = board[end_r][end_c]
                if end_sq == '--' :
                    moves.append((board[end_r][end_c]))
                elif end_sq[0] == enemy:
                    moves.append((board[end_r][end_c]))
                    break
bishop_move(row,column,moves)
rook_move(row,column,moves)
print(moves)