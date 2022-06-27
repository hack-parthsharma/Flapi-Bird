import pygame
import config as cfg

def collision_detection(bird, pipe):
    """
    Detects whether the bird has collided with the pipe.

    input params: 
        Bird() and Pipe() objects

    output params:
        True if collision occured
        or False value if not.
    """

    # converting the
    top_pipe = pygame.Rect(pipe.left, pipe.top_pipe_top, pipe.width, pipe.top_pipe_height)
    bottom_pipe = pygame.Rect(pipe.left, pipe.bottom_pipe_top, pipe.width, pipe.bottom_pipe_height)

    bird_box = pygame.Rect(
        bird.x,
        bird.y,
        cfg.BIRD_SIZE,
        cfg.BIRD_SIZE
        )

    if pygame.Rect.colliderect(top_pipe, bird_box)\
        or pygame.Rect.colliderect(bottom_pipe, bird_box):
        return True

    return False