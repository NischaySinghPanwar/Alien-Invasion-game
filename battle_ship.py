import pygame
class Ship():
    def __init__(self,screen):
        """initialize the ship and its starting positon"""
        self.screen=screen
        # loding the iamge of battle_ship
        self.image=pygame.image.load('D:\TEMPERORY\mistershaft PYTHON\invasion\img\ship.bmp')
        self.rect= self.image.get_rect()
        self.screen_rect = screen.get_rect()
         
        #  this will start eaach ship at the bottom of the screen
        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom =self.screen_rect.bottom
        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update (self):
        """update the ship movement based on the flag"""
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1

    def blitme(self):
        """draw the ship at its location."""
        self.screen.blit(self.image,self.rect)

