#PyGame_OOPs_Programming_8
# Write your code here :-)
#ethernet_game_image/drawn objects file
import pygame
pygame.init()

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
pictile_x_position =   50
pictile_y_position =   100
pictile_width      =   100
pictile_height     =   100
pictile_colour     =   BLUE
piclabel           =   "new"


dice_tile_x_position =   50
dice_tile_y_position =   100
dice_tile_width      =   100
dice_tile_height     =   100
dice_tile_colour     =   RED
dice_tile_label      =   "Go On"







class Picture_Tile(object):
    def __init__(self, pictile_x_position,pictile_y_position, pictile_width, pictile_height     ):
        pygame.sprite.Sprite.__init__(self)
        self.pictile_width  = pictile_width
        self.pictile_height = pictile_height
        self.image          = pygame.image.load("./Test_tile_image1.png")


        self.image          = pygame.transform.scale(self.image,(self.pictile_width,self.pictile_height))#Transform and scale functions resize a .png image
        self.image_rect     = self.image.get_rect()
        self.image_rect.x   = self.image_rect.x
        self.image_rect.y   = self.image_rect.y
        self.rect           = self.image.get_rect( )#retrieves tuple rectangle/surface data (x, y, width, height)
        self.rect           = (self.rect.x , self.rect.y)

        #self.tile_image = pygame.Surface((self.tile_width,self.tile_height)) #Creates a Surface((width,height)) Surfaces can be hardware accelerated
        #self.tile_image.fill(self.tile_colour) #fill the tile_surface with a colour (R,G,B)


#pic_tile_1 = Picture_Tile(pictile_x_position,pictile_y_position, pictile_width, pictile_height )
def Roll_It(dice_roll):
    dice_roll = dice_roll
    rollCount = 0

    dice_list =[pygame.image.load("./Test_tile_image1.png"),
                pygame.image.load("./Test_tile_image2.png"),
                pygame.image.load("./Test_tile_image3.png"),
                pygame.image.load("./Test_tile_image4.png"),
                pygame.image.load("./Test_tile_image5.png"),
                pygame.image.load("./Test_tile_image6.png") ]


    if rollCount +1 >= 30:#if rollCount exceed 30 then End of Index error would occur... hence the reset
        rollCount = 0 #30 frames / 6 images = 5 images per second???

    if dice_roll:
        window.blit(dice_list[rollCount//5], (300,300))
        rollCount += 1

