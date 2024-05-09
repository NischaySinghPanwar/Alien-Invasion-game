
import pygame
from settings import Settings
from battle_ship import Ship
import game_functions as gf


def run_game():
    # initialize pygame , setting, screen object.
    pygame.init()
    Ai_setting=Settings()
    screen = pygame.display.set_mode((Ai_setting.screen_width,Ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # to display the ship in screen 
    ship=Ship(screen)
    

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(Ai_setting,screen,ship)

run_game()
