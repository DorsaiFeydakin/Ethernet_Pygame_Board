#PyGame_OOPs_Programming_8
# Write your code here :-)
#ethernet_game_image/drawn objects file
import pygame

window_width=800
window_height=500

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


dice_tile_x_position =   50
dice_tile_y_position =   100
dice_tile_width      =   100
dice_tile_height     =   100
dice_tile_colour     =   RED
dice_tile_label      =   "Go On"



class Tile(pygame.sprite.Sprite):

    def __init__(self,tile_x_position, tile_y_position, tile_width, tile_height, tile_colour, label ):
        pygame.sprite.Sprite.__init__(self)


        ###we don't necessarily use all of these now that I have a .png file
        self.tile_x_position    = tile_x_position
        self.tile_y_position    = tile_y_position
        self.tile_width         = tile_width #not needed now we are using an image???
        self.tile_height        = tile_height #not needed now we are using an image???
        self.tile_colour        = tile_colour #not needed now we are using an image???
        self.text_label         = label ###we definitely use this variable though

        self.tile_surface       = pygame.Surface((self.tile_width,self.tile_height)) #Surface((width,height))
        self.tile_surface.fill(self.tile_colour)
        self.tile_rectangle     = self.tile_surface.get_rect( )
        #print("This is the self.tile_rectangle tuple... ", self.tile_rectangle )


        ###Creates a surface with Text rendered on top of it
        self.textsurface             = pygame.font.SysFont('consolas', 30).render(self.text_label, True, (0,0,0))
        self.textSurfaceRectangle    = self.textsurface.get_rect()#should hopefully create a rectangle for the rendered text
        self.textSurfaceRectangle.x  = self.textSurfaceRectangle.x
        self.textSurfaceRectangle.y  = self.textSurfaceRectangle.y
        #print ("self.textSurfaceRectangle coordinates are...", self.textSurfaceRectangle )





        self.text_position    = (self.tile_x_position+(self.tile_width/3), self.tile_y_position+(self.tile_height/3))
        #self.textsurface.blit(self.textsurface, self.text_position)#should place the text surface to the screen
        #print("This is self.image printed as  ",self.image)
        #print("This is what textrect looks like.....",self.text_position)




    def isOver(self, position):
        if position[0] > self.tile_x_position and position[0] < self.tile_x_position + self.tile_width:
            if position[1] > self.tile_y_position and  position[1] < self.tile_y_position + self.tile_height:
                return True
        return False




"""
class Rollover_Tile(Tile):#inherits a lot of properties from the parent class called Tile (I hope)
        def __init__(self):
            ####PNG file that is then scaled down to size
            self.image          = pygame.image.load("/Users/seamusmcginley/Documents/eKIT/Python_Programming/PyGAME_OOPs_Hybrids_programming_3/Test_tile_image.png")
            self.image          = pygame.transform.scale(self.image,(self.tile_width,self.tile_height))#Transform and scale functions resize a .png image
            self.image_rect     = self.image.get_rect()
            self.image_rect.x   = self.image_rect.x
            self.image_rect.y   = self.image_rect.y
            self.rect           = self.image.get_rect( )#retrieves tuple rectangle/surface data (x, y, width, height)
            self.rect           = (self.rect.x , self.rect.y)

            #self.tile_image = pygame.Surface((self.tile_width,self.tile_height)) #Creates a Surface((width,height)) Surfaces can be hardware accelerated
            #self.tile_image.fill(self.tile_colour) #fill the tile_surface with a colour (R,G,B)
"""
