from chess_engine import Board
from chess_engine import Move_Piece 
import pygame

WIDTH = HEIGHT = 480            #setting up the width and height of chess board
DIMENSIONS = 8                  #number of squares on one side 
SQ_SIZE = HEIGHT // DIMENSIONS  
BACKGROUND = (0,0,0)            #colour of the background. probably not needed
FPS = 60                        #speed of refresing in which we refresh and redraw the game
BLACK = (125,148,93)            #color for black squares
WHITE = (238,238,213)           #color for white squares
IMAGES = dict()                 #dictionary of image pieces

class Window():                                             #setting up window class where all the game redrawing is going to happend. 
    def __init__(self):
        self.WIDTH= WIDTH
        self.HEIGHT= HEIGHT
        self.BACKGROUND = BACKGROUND
        self.FPS = FPS
        self.win = pygame.display.set_mode((WIDTH,HEIGHT))  #dimension of game window
        pygame.display.set_caption('Chess')                 #title of the window of game
        self.b = Board()                                    #instentiating the chess logic class from chess_engine.py

    def draw_board(self):
        for column in range(DIMENSIONS):    #drawing the rectangulars of chess board. iterating over column and row if column and row is 
            for row in range(DIMENSIONS):   #odd it is light and if even it's dark
                if ((column+row)%2) == 1: 
                    self.black_rect = pygame.Rect((row*SQ_SIZE),(column*SQ_SIZE),SQ_SIZE,SQ_SIZE)   #create rect on x,y position of SQ_size
                    pygame.draw.rect(self.win, BLACK, self.black_rect) 
                else:
                    self.white_rect = pygame.Rect((row*SQ_SIZE),(column*SQ_SIZE),SQ_SIZE,SQ_SIZE)   #create rect on x,y position of SQ_size
                    pygame.draw.rect(self.win, WHITE, self.white_rect) 

    def draw_window(self):
        self.win.fill(self.BACKGROUND)  #draw a window with background 
        self.draw_board()               #draw board
        self.draw_pieces()              #draw pieces on top of the board
        pygame.display.update()
        pygame.display.flip()

    def draw_pieces(self):
        for row in range(DIMENSIONS):
            for column in range(DIMENSIONS):
                if (self.b.board[row][column]) !='--':
                    self.piece_rect = self.win.blit(IMAGES[(self.b.board[row][column])],pygame.Rect((column*SQ_SIZE), (row*SQ_SIZE),SQ_SIZE,SQ_SIZE))

    def clock_speed(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)

    def pieces_images(self):
        self.pieces = ['bR','bB','bQ','bK','bN','bP','wR','wB','wQ','wK','wN','wP']
        for piece in self.pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQ_SIZE,SQ_SIZE))


def main():
    w = Window()
    b = w.b
    w.pieces_images()
    #legal_move return as list of legal moves.   
    sq_sel = ()
    player_clicks = []
    #running game while loop
    run = True 
    while run:
        valid_move = b.legal_move()
        move_check = False
        w.clock_speed() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #if a click a left button on mouse the logic gets executed
            elif event.type == pygame.MOUSEBUTTONDOWN:                  
            #return x and y coordinance of cursor
                m_x, m_y = pygame.mouse.get_pos()                       
            #dividing x coordinant of mouse by sq_size to get row on the chess board
                column = m_x//SQ_SIZE                                   
            #dividing y coordinant of mouse by sq_size to get column on the chess board
                row = m_y//SQ_SIZE                                     
            #if same sq is selected undo the move
                if sq_sel == (column,row):   
                    sq_sel = ()
                    player_clicks = []
                else:
            #tuple with the actual square position of mouse(column, row)
                    sq_sel = (column, row)                               
            #we take the tuple(column, row) and append the piece that is actually on that position
                    player_clicks.append([sq_sel[1], sq_sel[0]])        
            #when the lenght of list if 2 that mean we have all moves     
                if len(player_clicks) == 2:
                    #take the move that was made and check if it is legal.
                    move = Move_Piece(player_clicks[0],player_clicks[1], b.board)      
                    if move in valid_move:
                        #when move is legal. Change the board. Set the move_check equal to true and set tuple and list to empty.
                        b.move_on_board(move)
                        move_check = True
                        sq_sel = ()
                        player_clicks = []        
                    elif move not in valid_move:
                        player_clicks = [sq_sel]

        if move_check :
            valid_move = b.legal_move() 
            move_check = False

        w.draw_window()
    pygame.quit()   

if __name__ == '__main__':
    main()