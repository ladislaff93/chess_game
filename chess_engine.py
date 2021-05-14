class Board():
    def __init__(self):
        #first character is b or w (black or white), next character pieces
        # . R-Rook, P-Pawn
        #N-knight, B-bishop, Q-queen, K-king.
        self.board=[
            [["bR"],["bN"],["bB"],["bQ"],["bK"],["bB"],["bN"],["bR"]],
            [["bP"],["bP"],["bP"],["bP"],["bP"],["bP"],["bP"],["bP"]],
            [['--'],['--'],['--'],['--'],['--'],['--'],['--'],['--']],
            [['--'],['--'],['--'],['--'],['--'],['--'],['--'],['--']],
            [['--'],['--'],['--'],['--'],['--'],['--'],['--'],['--']],
            [['--'],['--'],['--'],['--'],['--'],['--'],['--'],['--']],            
            [["wP"],["wP"],["wP"],["wP"],["wP"],["wP"],["wP"],["wP"]],
            [["wR"],["wN"],["wB"],["wQ"],["wK"],["wB"],["wN"],["wR"]]
        ]
        self.white_first = True                                                                         #logic for white first move. 
        print('WHITE IS ON THE MOVE!')
        self.move_log = []                                                                              #move log for algebraic notation    
  
    def move_on_board(self, move):
        self.board[move.start_row][move.start_column]=['--']
        self.board[move.end_row][move.end_column]=move.piece_moved
        #self.move_log.append(move.piece_moved)
        #self.move_log.append(move.piece_captured)
        move.algebraic_notation(self.move_log)                                                                   
        self.white_first = not self.white_first
        print('PIECE '+self.move_log[0]+' MOVE TO '+self.move_log[1])   
        if not self.white_first:
            print('BLACK IS ON THE MOVE!')
        else:
            print('WHITE IS ON THE MOVE!')    
        if len(self.move_log) == 2:
            self.move_log = []    
        
    def check_move(self):
        return self.piece_move()

    def piece_move(self):
        moves = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                turn = self.board[row][column][0][0]
                if turn == 'w' and self.white_first or turn == 'b' and not self.white_first:
                    piece = self.board[row][column][0][1]
                    if piece == 'P':
                       self.pawn_move(row,column,moves) 
                    elif piece == 'R':
                        pass
        return moves
       
    def pawn_move(self, row, column, moves):
        if self.white_first and row == 6:
            if self.white_first:
                if self.board[row-1][column] == ['--']:
                    moves.append(Move_Piece((row,column),(row-1,column),self.board))
                    if row == 6 and self.board[row-2][column] == ['--']:   
                        moves.append(Move_Piece((row,column),(row-2,column), self.board))


    def rook_move(self):
        pass


class Move_Piece():
    def __init__(self, start_sq, end_sq, board):                          #engine part of moving pieces. we take start and end squares from chess_main-->move pieces-->player_clicks list
        self.start_row = start_sq[0]                                                                    #from chess_main start_sq start row
        self.start_column = start_sq[1]                                                                 #from chess_main start_sq start column
        self.end_row = end_sq[0]                                                                        #from chess_main start_sq end row
        self.end_column = end_sq[1]                                                                     #from chess_main start_sq end column
        self.piece_moved = board[self.start_row][self.start_column]                                #variable of piece first selected
        self.piece_captured = board[self.end_row][self.end_column]                                 #variable of piece selected second
 
    def algebraic_notation(self, move_log):
        self.numbers = ['8','7','6','5','4','3','2','1']                        #numbers for row 
        self.letters = ['a','b','c','d','e','f','g','h']                        #letters for column
        self.start_column_letters = self.letters[self.start_column]             
        self.start_row_numbers = self.numbers[self.start_row]                   
        self.end_column_letters = self.letters[self.end_column]
        self.end_row_numbers = self.numbers[self.end_row]
        move_log.append(self.start_column_letters+self.start_row_numbers)
        move_log.append(self.end_column_letters+self.end_row_numbers)


if __name__ == '__main__':
    board = Board()
    print(board.board())

#when white on move and if white pieces are in the way print message 'INVALID MOVE!!' 
#en passant 
#pawn changing in base aka Pawn Promotion
#rosada mala velka aka Castling