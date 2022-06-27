import pygame
import config as cfg
import random

class Pipes():
    def __init__(self):
        # Design & Physics
        self.width = cfg.PIPE_WIDTH
        self.left = cfg.SCREEN_WIDTH
        
        self.bottom_pipe_top = random.randint(cfg.PIPE_RANGE_FROM_TOP, \
            cfg.SCREEN_HEIGHT - cfg.PIPE_RANGE_FROM_BOTTOM)
        self.bottom_pipe_height = cfg.SCREEN_HEIGHT - self.bottom_pipe_top
        self.top_pipe_top = 0 
        self.top_pipe_height = cfg.SCREEN_HEIGHT - self.bottom_pipe_height - cfg.PIPE_GAP
        
        # Physics
        self.v = cfg.PIPE_VELOCITY

    def move(self):
        """
        Checks whether the pipe has gone out of the screen on the
        left hand side. 

        returns true if the pipe is still on the screen,
        else returns false.
        """
        self.left += self.v
        
        # check boudary crossing
        if self.left <= -cfg.PIPE_WIDTH:
            return False

        return True

    def draw(self):
        # draws the top and the bottom pipes
        
        pygame.draw.rect(cfg.SCREEN, cfg.GREEN, \
            (self.left, self.top_pipe_top, self.width, self.top_pipe_height))        

        pygame.draw.rect(cfg.SCREEN, cfg.GREEN, \
            (self.left, self.bottom_pipe_top, self.width, self.bottom_pipe_height))       

