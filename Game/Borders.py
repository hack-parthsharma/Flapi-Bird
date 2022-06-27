import pygame
import config as cfg

def draw():
    # draws the top and bottom bird death zones.
    pygame.draw.rect(cfg.SCREEN, cfg.DARK_BLUE, 
        (0, cfg.SCREEN_HEIGHT-cfg.GROUND_HEIGHT, cfg.SCREEN_WIDTH, cfg.GROUND_HEIGHT)
    )

    pygame.draw.rect(cfg.SCREEN, cfg.LIGHT_BLUE, 
        (0, 0, cfg.SCREEN_WIDTH, cfg.SKY_HEIGHT)
    )

def scorer(score):
    # displays the current score on the screen top-left corner
    text = cfg.font.render(
        str(score).encode('utf-8').decode('utf-8'), True, cfg.WHITE
    )
    cfg.SCREEN.blit(text, (0, 0))
