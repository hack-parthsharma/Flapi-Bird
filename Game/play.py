from Birds import Bird
from Pipes import Pipes
import Borders
import config as cfg
import time
from Utility import collision_detection

import pygame
pygame.init()

# Score to be displayed
score = 0

# yey, birb!
bird = Bird()
# pipes
pipes = []
pipe = Pipes()
pipes.append(pipe)

running = True
while running:

    # score for each frame you stay alive
    score += 0.005 
    
    # Handling exit and jumps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()


    # UPDATING OBJECTS        
    ## bird
    bird_alive =  bird.move()
    ## pipes: destruction
    for pipe in pipes:
        if not pipe.move():
            del pipe
    ## pipes: generation        
    if pipes[-1].left <= cfg.SCREEN_WIDTH - cfg.PIPE_WIDTH - cfg.PIPE_SPACER:
        pipes.append(Pipes())


    # COLLISION DETECTION
    for pipe in pipes:
        if collision_detection(bird, pipe):
            bird_alive = False
            break
    
    # DRAWING OBJECTS
    ## fill screen with background
    cfg.SCREEN.fill(cfg.BLUE)
    ## pipes
    for pipe in pipes:
        pipe.draw()
    ## bird
    if bird_alive:
        bird.draw()
    else:
        bird.color = cfg.RED
        bird.draw()
        del bird
        running = False

    # UPDATE SCREEN
    Borders.draw()
    Borders.scorer(int(score))
    pygame.display.update()

    # game over
    if not running:
        time.sleep(cfg.BIRD_DEATH_TIME)

if(score < 20):
    print(f"Game Over \nYou scored: {int(score)} points. Sad.")
elif(score < 50):
    print(f"Game Over \nYou scored: {int(score)} points!")
else:
    print(f"Game Over \nYou scored: {int(score)} points. Yeet!")