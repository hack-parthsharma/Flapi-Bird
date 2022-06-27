import pygame
import config as cfg
import time
import random

class Bird():
    def __init__(self):
        # Design
        self.color = cfg.BIRD_COLOR

        # PHYSICS
        # As given in the config file
        ## Positions
        self.x = cfg.BIRD_X_INIT
        self.y = random.randint( \
            cfg.BIRD_SIZE + cfg.SKY_HEIGHT + cfg.BIRD_SPACER_INIT, \
            cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE - cfg.BIRD_SPACER_INIT)
        ## Time
        self.t = 0
        ## Velocities
        self.v = cfg.BIRD_INITIAL_VELOCITY
        self.tv = cfg.BIRD_TERMINAL_VELOCITY
        ## Accleration
        self.g = cfg.GRAVITY

    def jump(self):
        """
        Makes the bird Jump
        """
        # reset time for falling
        self.t = 1
        # point velocity vector upwards
        self.v = cfg.BIRD_UPWARD_VELOCITY
        # move the bird upwards (technically not required.)
        self.y += cfg.BIRD_JUMP_HEIGHT

    def move(self):
        """
        - Makes the bird fall due to the action of gravity.
        - Checks whether the bird is too high or too low.

        Returns False as in 'don't move the bird (its ded :()'
        else True as in 'keep the bird alive'
        """
        # time
        self.t += 1

        # velocity
        self.v = self.v + self.g * self.t
        if self.v >= self.tv:
            self.v = self.tv

        # displacement
        self.y = self.y + self.v * self.t + 0.5 * self.g * self.t**2

        # # Top Stop
        # if self.y <= cfg.BIRD_SIZE + cfg.SKY_HEIGHT:
        #     self.y = cfg.BIRD_SIZE + cfg.SKY_HEIGHT

        # Top also death
        if self.y <= cfg.BIRD_SIZE + cfg.SKY_HEIGHT:
            self.y = cfg.BIRD_SIZE + cfg.SKY_HEIGHT
            return False
            
        # Bottom DEATH
        if self.y >= (cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE):
            self.y = cfg.SCREEN_HEIGHT - cfg.GROUND_HEIGHT - cfg.BIRD_SIZE
            return False

        # Birb still alive!
        return True

    def draw(self):
        # self explanatory ;)
        pygame.draw.circle(cfg.SCREEN, self.color, (int(self.x), int(self.y)), cfg.BIRD_SIZE)