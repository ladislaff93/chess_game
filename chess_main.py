'''
Importing from modules
'''
from chess_engine import Board
from chess_engine import Move_Piece 
import pygame
import gui

'''
Instantiating a classes
'''
w = gui.Window()

'''
Defining main function where game is running
'''
def main():
    w.pieces_images()
    #legal_move return as list of legal moves.   
    sq_sel = ()
    player_clicks = []
    #running game while loop
    run = True 
    while run:
        valid_move = gui.board.legal_move()
        move_check = False
        w.clock_speed() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #if a click a left.board.tton on mouse the logic gets executed
            elif event.type == pygame.MOUSEBUTTONDOWN:                  
            #return x and y coordinance of cursor
                m_x, m_y = pygame.mouse.get_pos()                       
            #dividing x coordinant of mouse.board. sq_size to get row on the chess.board.ard
                column = m_x//gui.SQ_SIZE                                   
            #dividing y coordinant of mouse.board. sq_size to get column on the chess.board.ard
                row = m_y//gui.SQ_SIZE                                     
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
                    move = Move_Piece(player_clicks[0],player_clicks[1], gui.board.board)      
                    if move in valid_move:
                        #when move is legal. Change the.board.ard. Set the move_check equal to true and set tuple and list to empty.
                        gui.board.move_on.board.ard(move)
                        print(gui.board.legal_move())
                        move_check = True
                        sq_sel = ()
                        player_clicks = []        
                    else:
                        player_clicks = [sq_sel]

            elif event.type == pygame.KEYDOWN:                  
                if event.type == pygame.K_LEFT:
                    gui.board.undo_move()

        if move_check :
            valid_move = gui.board.legal_move() 
            move_check = False

        w.draw_window()
    pygame.quit()   

if __name__ == '__main__':
    main()