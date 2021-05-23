class Board():
    def __init__(self):
        #first character is b or w (black or white), next character pieces
        # . R-Rook, P-Pawn
        #N-knight, B-bishop, Q-queen, K-king.
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],            
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.white_first = True                                       #logic for white first move. 
        print('WHITE IS ON THE MOVE!')
        self.move_log = []                                            #move log for algebraic notation    
  
    def move_on_board(self, move):
        self.board[move.start_row][move.start_column] = '--'              #change the start square after moving piece
        self.board[move.end_row][move.end_column] = move.piece_moved      #change the end square on start square
        move.algebraic_notation(self.move_log)                          #return algebraic notation for actual move.                                             
        self.white_first = not self.white_first
        print('PIECE '+self.move_log[0]+' MOVE TO '+self.move_log[1])   
        
        if not self.white_first:
            print('BLACK IS ON THE MOVE!')

        elif self.white_first:
            print('WHITE IS ON THE MOVE!')    

        if len(self.move_log) == 2:
            self.move_log = []    

    #function for checking if the move what we made is actually legal.    
    #If the current move dont compromise the king piece(capturning).
    def legal_move(self): 

        return self.piece_move()   

    def piece_move(self): #for every piece on board function define it possible moves. And whose turn is(b or w)
        moves = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                turn = self.board[row][column][0]
                if turn == 'w' and self.white_first or turn == 'b' and not self.white_first: 
                    piece = self.board[row][column][1]                                       
                    if piece == 'P':
                       self.pawn_move(row, column, moves) 
                    elif piece == 'R':
                       self.rook_move(row, column, moves)
                    elif piece == 'Q':
                        self.queen_move(row, column, moves)
                    elif piece == 'K':
                        self.king_move(row, column, moves)
                    elif piece == 'N':
                        self.knight_move(row, column, moves)
                    elif piece == 'B':
                        self.bishop_move(row, column, moves)
        return moves

    def queen_move(self, row, column, moves):
        self.bishop_move(row,column,moves)
        self.rook_move(row,column, moves)

    def king_move(self, row, column, moves):
        direction = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        enemy = 'b' if self.white_first else 'w'
        for d in direction:
            end_r = row + d[0] 
            end_c = column + d[1]  
            if 0 <= end_r <=7 and 0 <= end_c <=7:
                end_sq = self.board[end_r][end_c]
                if end_sq == '--' or end_sq[0] == enemy:
                    moves.append(Move_Piece((row,column), (end_r,end_c), self.board))
                else:
                    break

    def knight_move(self, row, column, moves):
        direction = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2))
        enemy = 'b' if self.white_first else 'w'
        for d in direction:
            end_r = row + d[0] 
            end_c = column + d[1]  
            if 0 <= end_r <=7 and 0 <= end_c <=7:
                end_sq = self.board[end_r][end_c]
                if end_sq == '--' or end_sq[0] == enemy:
                    moves.append(Move_Piece((row,column), (end_r,end_c), self.board))

    def bishop_move(self, row, column, moves):
        direction = ((1,1),(-1,1),(1,-1),(-1,-1))
        enemy = 'b' if self.white_first else 'w'
        for d in direction:
            for l in range(1,(len(self.board))):
                end_r = row + l*d[0] 
                end_c = column + l*d[1] 
                if 0 <= end_r <= 7 and 0 <= end_c <= 7:
                    end_sq = self.board[end_r][end_c]
                    if end_sq == '--' :
                        moves.append(Move_Piece((row,column), (end_r,end_c), self.board))
                    elif end_sq[0] == enemy:
                        moves.append(Move_Piece((row,column), (end_r,end_c), self.board))
                    else:
                        break

    def rook_move(self, row, column, moves): #rook move logic. Rook can move in perpendicular way and for full lenght of the board (in cross.)
        direction = ((1,0),(-1,0),(0,1),(0,-1))
        enemy = 'b' if self.white_first else 'w'
        for d in direction:
            for l in range(1,(len(self.board))):
                end_r = row + l*d[0] 
                end_c = column + l*d[1]  
                if 0 <= end_r <=7 and 0 <= end_c <=7:
                    end_sq = self.board[end_r][end_c]
                    if end_sq == '--' :
                        moves.append(Move_Piece((row,column), (end_r,end_c), self.board))
                    elif end_sq[0] == enemy:
                        moves.append(Move_Piece((row,column), (end_r,end_c), self.board))
                        
                    else:
                        break

    def pawn_move(self, row, column, moves): #defining the piece moving logic. Pawn can move 2 or 1 square if is in start position or 1 if its not. 
        if self.white_first: 
            if self.board[row-1][column] == '--':
                moves.append(Move_Piece((row,column),(row-1,column),self.board))
                if row == 6 and self.board[row-2][column] == '--':   
                    moves.append(Move_Piece((row,column),(row-2,column), self.board))
                    
            if column+1 <= 7 and 0 < row-1: #capturing to the right
                if self.board[row-1][column+1][0] == 'b':
                    moves.append(Move_Piece((row,column),(row-1,column+1),self.board))
                
            if 0 < column-1 and 0 < row-1:
                if self.board[row-1][column-1][0] == 'b': #capturing piece to the left 
                    moves.append(Move_Piece((row,column),(row-1,column-1),self.board))
                    
        else:
            if self.board[row+1][column] == '--':
                moves.append(Move_Piece((row,column),(row+1,column), self.board)) 
                if row == 1 and self.board[row+2][column] == '--':
                    moves.append(Move_Piece((row,column),(row+2,column), self.board))
         
            if column + 1 <= 7 and row + 1 <= 7: #capturing to the right 
                if self.board[row+1][column+1][0] == 'w':
                    moves.append(Move_Piece((row,column),(row+1,column+1),self.board))
                
            if 0 < column-1 and row+1 <= 7:
                if self.board[row+1][column-1][0] == 'w': #capturing to the left 
                    moves.append(Move_Piece((row,column),(row+1,column-1),self.board))

class Move_Piece():
    def __init__(self, start_sq, end_sq, board):                          #engine part of moving pieces. we take start and end squares from chess_main-->move pieces-->player_clicks list
        self.start_row = start_sq[0]                                                                    #from chess_main start_sq start row
        self.start_column = start_sq[1]                                                                 #from chess_main start_sq start column
        self.end_row = end_sq[0]                                                                        #from chess_main start_sq end row
        self.end_column = end_sq[1]                                                                     #from chess_main start_sq end column
        self.piece_moved = board[self.start_row][self.start_column]                                #variable of piece first selected
        self.piece_captured = board[self.end_row][self.end_column]                                 #variable of piece selected second
        self.ID = self.start_row*1000+self.start_column*100+self.end_row*10+self.end_column

    def __eq__(self, other): 
        if isinstance(other, Move_Piece):
            return self.ID == other.ID
        return False 

    def algebraic_notation(self, move_log):
        #numbers for row
        self.numbers = ['8','7','6','5','4','3','2','1']                         
        #letters for column
        self.letters = ['a','b','c','d','e','f','g','h']                        
        self.start_column_letters = self.letters[self.start_column]             
        self.start_row_numbers = self.numbers[self.start_row]                   
        self.end_column_letters = self.letters[self.end_column]
        self.end_row_numbers = self.numbers[self.end_row]
        move_log.append(self.start_column_letters+self.start_row_numbers)
        move_log.append(self.end_column_letters+self.end_row_numbers)


#en passant 
#pawn changing in base aka Pawn Promotion
#rosada mala velka aka Castling