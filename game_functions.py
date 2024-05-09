import sys
import pygame
from settings import Settings

def check_events(ship):
    """respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                    #  move the dhip to the right0 /
                    ship.moving_right = True
            elif event.key ==pygame.K_LEFT:
                 pass
             
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_RIGHT:
                 ship.moving_right = False

def update_screen(Ai_settings,screen,ship):
    """updating images on the screen and filp to the new screen [ by deleting the old screen]"""
     # redrawing the screen each pass through loop
    screen.fill(Ai_settings.background_color)
    ship.blitme()
        # it will redraw the new screen at the end of the loop 
        # it will delete the od screen and replace it with new one
        # continually update the display to show the new positions of       elements and
        # hide the old ones, creating the illusion of smooth movement.
    pygame.display.flip()