#PyGame_OOPs_Programming_2
##Hoping to combine skills learned so far from..
###PyGame Tutorials and Raspberry Pi OOPs Course
####using multiple files to keep things tidy and easier to use.
#####This file is the LOGICAL ACTION file.


import pygame
import random
from ethernet_game_drawn_objects import Tile
from ethernet_game_picture_tile_library import Picture_Tile
from dice_roll_file import Dice_Roller
import time
pygame.init()



####################################################################################
##############################Useful Variabes START#######################################

#VARIABLE COLOURS RGB
WHITE   =   (255,255,255)
BLACK   =   (0,0,0)
RED     =   (255,0,0)
LIME    =   (0,255,0)
BLUE    =   (0,0,255)
YELLOW  =   (255,255,0)
CYAN    =   (0,255,255)
MAGENTA =   (255,0,255)
SILVER  =   (192,192,192)
GRAY    =   (128,128,128)
MAROON  =   (128,0,0)
OLIVE   =   (128,128,0)
GREEN   =   (0,128,0)
PURPLE  =   (128,0,128)
TEAL    =   (0,128,128)
NAVY    =   (0,0,128)

#Origin Tile Variables
tile_x_position =   50
tile_y_position =   100
tile_width      =   100
tile_height     =   100
tile_colour     =   BLUE
label           =   "new"


##############################Useful Variabes END###################################
####################################################################################

######sets up the initial window and environment. e.g. Background Colour, font-type, FPS rate etc. #######
class Ethernet_Game_Window(object):
    def __init__(self, window_width=800, window_height=500, FPS=30):
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.window_width = window_width # sets width of window
        self.window_height = window_height #set height of window
        self.window = pygame.display.set_mode((self.window_width, self.window_height))


        self.clock = pygame.time.Clock()
        self.FPS = FPS #frame rate
        self.playtime = 0.0


        self.font = pygame.font.SysFont('mono', 24, bold=True)#sets the system protocols for text in the game






    def Mainloop(self):

        #Creates instances of a game tile objects


        #stores all our sprites  after they've done what they are supposed to do
        #all_sprites = pygame.sprite.Group()


        ####Section where instances of objects are created####
        tile1       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "Preamble")
        tile2       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "DA")
        tile3       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "SA")
        tile4       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "TOS/Length")
        tile5       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "Data")
        tile6       =    Tile(tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, "Checksum")






                                    #pictile_x_position, pictile_y_position, pictile_width, pictile_height
        picTile1    =    Picture_Tile(tile_x_position,   tile_y_position,    tile_width,    tile_height)

        #all_sprites.add(tile1, tile2, tile3)


        dice_sprites    = pygame.sprite.Group()
        dice1           = Dice_Roller(400, 320)
        dice_sprites.add(dice1)

        winning_sprite_numbers = []
        runtime = True
        while runtime: #same as saying while runtime == True

            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                #print (event)


                #returns a tuple with mouse (x,y) coordinates
                position = pygame.mouse.get_pos()
                #print ("Mouse position is currently at " + str(position))

                #runtime is switched to False or "OFF" if user detected clicking x at top of window
                if event.type == pygame.QUIT:
                    runtime = False

                #runtime is switched to False or "OFF" if user detected pressing ESC on keyboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        runtime = False

                    elif event.key == pygame.K_SPACE:
                        #print("Space bar pressed.")
                        dice_roll = True

                    elif event.key == pygame.K_r:
                        dice1.animate()#calls the animate function on that particular object

                        winning_sprite_numbers.append(dice1.current_sprite)
                        print ("current_sprite = " ,dice1.current_sprite)
                        print (winning_sprite_numbers)


                        if dice1.current_sprite == 1:
                            tile1 = Tile(tile_x_position, tile_y_position, tile_width, tile_height, CYAN,  "PRE")


                        elif dice1.current_sprite == 2:
                            tile2 = Tile(tile_x_position+(tile_width*1+10), tile_y_position, tile_width, tile_height, CYAN,"DA")


                        elif dice1.current_sprite == 3:
                            tile3 = Tile(tile_x_position+(tile_height*2+20), tile_y_position, tile_width, tile_height, CYAN,  "SA")


                        elif dice1.current_sprite == 4:
                           tile4 = Tile(tile_x_position+(tile_width*3+30), tile_y_position, tile_width, tile_height, CYAN,  "TOS")

                        elif dice1.current_sprite == 5:
                            tile5 = Tile(tile_x_position+(tile_width*4+40), tile_y_position, tile_width, tile_height, CYAN,  "DATA")

                        elif dice1.current_sprite == 6:
                            tile6 = Tile(tile_x_position+(tile_width*5+50), tile_y_position, tile_width, tile_height, CYAN,  "Check")





                else:
                    #print("Not over the tiles")

                    tile1 = Tile(tile_x_position                     , tile_y_position, tile_width, tile_height, tile_colour,   "Pre"       )
                    tile2 = Tile(tile_x_position  +(tile_width*1+10 ), tile_y_position, tile_width, tile_height, tile_colour,   "DA"        )
                    tile3 = Tile(tile_x_position  +(tile_height*2+20), tile_y_position, tile_width, tile_height, tile_colour,   "SA"        )
                    tile4 =  Tile(tile_x_position +(tile_width*3+30 ), tile_y_position, tile_width, tile_height, tile_colour,   "TOS"       )
                    tile5 = Tile(tile_x_position  +(tile_height*4+40), tile_y_position, tile_width, tile_height, tile_colour,   "Data"      )
                    tile6 = Tile(tile_x_position  +(tile_height*5+50), tile_y_position, tile_width, tile_height, tile_colour,   "Check"     )


                if 1 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got one")
                    tile1 = Tile(tile_x_position, tile_y_position, tile_width, tile_height, CYAN,  "PRE")

                if 2 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got number 2")
                    tile2 = Tile(tile_x_position+(tile_width*1+10), tile_y_position, tile_width, tile_height, CYAN,"DA")

                if 3 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got number 3")
                    tile3 = Tile(tile_x_position+(tile_height*2+20), tile_y_position, tile_width, tile_height, CYAN,  "SA")

                if 4 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got number 4")
                    tile4 = Tile(tile_x_position+(tile_width*3+30), tile_y_position, tile_width, tile_height, CYAN,  "TOS")

                if 5 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got number 5")
                    tile5 = Tile(tile_x_position+(tile_width*4+40), tile_y_position, tile_width, tile_height, CYAN,  "DATA")

                if 6 in winning_sprite_numbers:#This shoud only work for tile 1 but apparently works for all????Gift horse???
                    print("We got number 6")
                    tile6 = Tile(tile_x_position+(tile_width*5+50), tile_y_position, tile_width, tile_height, CYAN,  "Check")




                if event.type == pygame.MOUSEBUTTONDOWN:
                    if tile1.isOver(position):
                        #print("Clicking on Tile 1 now")
                        tile1 = Tile(tile_x_position, tile_y_position, tile_width, tile_height, YELLOW,  "One") #Recreates an instance of "tile1" ...not efficient????
                        self.window.blit(tile1.tile_surface, [tile1.tile_x_position, tile1.tile_y_position])
                        self.window.blit(tile1.textsurface, tile1.text_position)#updates the screen with the tile surce created elsewhere


                    elif tile2.isOver(position):
                        #print("Clicking on Tile 2 now")
                        tile2 = Tile(tile_x_position+(tile_width*1+10), tile_y_position, tile_width, tile_height, YELLOW,"Two") #Recreates an instance of "tile2"


                    elif tile3.isOver(position):
                        #print("Clicking on Tile 3 now")
                        tile3 = Tile(tile_x_position+(tile_height*2+20), tile_y_position, tile_width, tile_height, YELLOW,  "Three") #Recreates an instance of "tile

                    else:
                        #print("Not over the tiles")
                        tile1      = Tile(tile_x_position, tile_y_position, tile_width, tile_height, BLUE,                     "PRE" )
                        tile2      = Tile(tile_x_position+(tile_width*1+10) , tile_y_position, tile_width, tile_height, BLUE,  "DA" )
                        tile3      = Tile(tile_x_position+(tile_height*2+20), tile_y_position, tile_width, tile_height, BLUE,  "SA")








            #############################################Draw/Render everything starts#########################################
            ############################################################################################################
            #while loop is running then next snippet
            #fills the window with a colour to leave a clear canvas for next set of objects
            self.window.fill(YELLOW)
            #all_sprites.draw(self.window)#uploads/draws all sprite objects en masse


            self.window.blit(tile1.tile_surface, [tile1.tile_x_position, tile1.tile_y_position])
            self.window.blit(tile1.textsurface, tile1.text_position)#updates the screen with the tile surce created elsewhere


            self.window.blit(tile2.tile_surface, [tile2.tile_x_position, tile2.tile_y_position])
            self.window.blit(tile2.textsurface, tile2.text_position)



            self.window.blit(tile3.tile_surface, [tile3.tile_x_position, tile3.tile_y_position])
            self.window.blit(tile3.textsurface, tile3.text_position)



            self.window.blit(tile4.tile_surface, [tile4.tile_x_position, tile4.tile_y_position])
            self.window.blit(tile4.textsurface, tile4.text_position)


            self.window.blit(tile5.tile_surface, [tile5.tile_x_position, tile5.tile_y_position])
            self.window.blit(tile5.textsurface, tile5.text_position)

            self.window.blit(tile6.tile_surface, [tile6.tile_x_position, tile6.tile_y_position])
            self.window.blit(tile6.textsurface,   tile6.text_position)


            dice_sprites.draw(self.window)
            dice_sprites.update(0.25)#updates the sprite group to the surface #0.25 is a speed value passed to the function














            pygame.display.flip()#updates the window display. #flip is meant to be a more efficient method
            #NB: flip is a Double Buffer process. Does work in background and then turns over page to present to user


            ############################################################################################################
            #################################Draw/Render everything ENDs#########################################
if __name__ == '__main__':
    Ethernet_Game_Window().Mainloop()
    # call with width of window and fps




pygame.quit()
quit()
#######################################################################
############## Create an instance of a tile object ####################





