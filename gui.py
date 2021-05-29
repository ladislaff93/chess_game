'''
Importing from modules
'''
from chess_engine import Board
from chess_engine import Move_Piece 
import pygame

'''
Defining the fundamental variables for py game 
'''
WIDTH = HEIGHT = 480            #setting up the width and height of chess board
DIMENSIONS = 8                  #number of squares on one side 
SQ_SIZE = HEIGHT // DIMENSIONS  
BACKGROUND = (0,0,0)            #colour of the background. probably not needed
FPS = 60                        #speed of refresing in which we refresh and redraw the game
BLACK = (125,148,93)            #color for black squares
WHITE = (238,238,213)           #color for white squares
IMAGES = dict()                 #dictionary of image pieces

'''
Instantiating a classes
'''
board = Board()                     

class Window():                                             #setting up window class where all the game redrawing is going to happend. 
    def __init__(self):
        self.WIDTH= WIDTH
        self.HEIGHT= HEIGHT
        self.BACKGROUND = BACKGROUND
        self.FPS = FPS
        self.win = pygame.display.set_mode((WIDTH,HEIGHT))  #dimension of game window
        pygame.display.set_caption('Chess')                 #title of the window of game

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
                if (board.board[row][column]) !='--':
                    self.piece_rect = self.win.blit(IMAGES[(board.board[row][column])],pygame.Rect((column*SQ_SIZE), (row*SQ_SIZE),SQ_SIZE,SQ_SIZE))

    def clock_speed(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)

    def pieces_images(self):
        self.pieces = ['bR','bB','bQ','bK','bN','bP','wR','wB','wQ','wK','wN','wP']
        for piece in self.pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQ_SIZE,SQ_SIZE))