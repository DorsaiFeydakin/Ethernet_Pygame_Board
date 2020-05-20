#PyGame_OOPs_Programming_8
# Write your code here :-)
#https://www.youtube.com/watch?v=MYaxPa_eZS0
#Dice Animation Project

import pygame, sys
import random
pygame.init()




class Dice_Roller(pygame.sprite.Sprite):
    def __init__(self, dicePosX, dicePosY):
        super().__init__()
        self.sprites = []

        self.is_animating = False #stops the animation from running until activated by True
        self.sprites.append(pygame.image.load("Test_tile_image.png" ))
        self.sprites.append(pygame.image.load("Test_tile_image1.png"))
        self.sprites.append(pygame.image.load("Test_tile_image2.png"))
        self.sprites.append(pygame.image.load("Test_tile_image3.png"))
        self.sprites.append(pygame.image.load("Test_tile_image4.png"))
        self.sprites.append(pygame.image.load("Test_tile_image5.png"))
        self.sprites.append(pygame.image.load("Test_tile_image6.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [dicePosX, dicePosY]

    def animate(self):
        self.is_animating = True

    def update(self, speed):

        if self.is_animating == True:
            self.current_sprite += speed #increments value: int version of 0.25 = 1 and won't change until it hits 2.0 or 2.25


            ####animates all the dice images using mainloop
            if self.current_sprite >= len(self.sprites):# checks how many sprites there are

                self.current_sprite = 0 #resets counter to zero when all sprites are used up
                self.is_animating = True #...but then keeps animating


                #######Random Dice image chosen
                RandomNumber = random.randint(1,6) #selects a random number
                print ("Random number = " ,RandomNumber)

                self.current_sprite = RandomNumber #uses the random number to decide which sprite image stays highlighted
                #print ("current_sprite = " ,self.current_sprite)

                self.is_animating = False #forces animation to stop at end of sequence



            ####animation sequence over..... the image of the chosen sprite is secured
            self.image = self.sprites[int(self.current_sprite)] #displays the rounded integer versionof the sprite














