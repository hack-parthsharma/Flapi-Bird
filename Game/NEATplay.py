from Birds import Bird
from Pipes import Pipes
import Borders
import config as cfg
import time
import neat
import os
from Utility import collision_detection

import pygame
pygame.init()

def neat_play(genomes, config):

    ## pipes init, as with 'play.py'
    pipes = [Pipes()]

    # AGLORITHM SETUP
    ## setups the neural nets and genes for each of the birds
    networks = []
    birds = []
    genes = []
    ## iterating through all the genomes
    ## genomes come from the population object
    for (_, genome) in genomes:
        genome.fitness = 0
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        networks.append(network)
        birds.append(Bird())
        genes.append(genome)


    # GAME LOOP
    ## runs while the user has not exited from the game
    ## and some birds still exist
    running = True
    while running and len(birds):

        # Handling exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        # UPDATING OBJECTS        
        ## Birds: Moving and Jumping
        ### feature: next pipe's index
        i = 0
        while pipes[i].left < birds[0].x:
            i += 1
        send_pipe_index = i
        ## go through all of the birds, move them 
        ## (with sky and ground logic as before),
        ## and check whether the bird's NN commands a jump
        birds_alive = []
        for i, bird in enumerate(birds):
            ### you get 0.01 point for staying alive each frame
            ### score
            genes[i].fitness += 0.01 
            ### moving the birds
            birds_alive.append(bird.move())
            ### sending inputs to NN
            predictions = networks[i].activate(
                (
                    bird.x,
                    bird.y,
                    pipes[send_pipe_index].left, 
                    cfg.PIPE_WIDTH,
                    bird.y - pipes[send_pipe_index].bottom_pipe_top, 
                    bird.y - pipes[send_pipe_index].top_pipe_height,
                    bird.y - pipes[send_pipe_index].bottom_pipe_height
                )
            )
            ### we only consider the first output of the network
            if predictions[0] > 0.5:
                bird.jump()

        ## Updating: Pipes: destruction
        for pipe in pipes:
            if not pipe.move():
                del pipe
        ## Updating: Pipes: generation        
        if pipes[-1].left <= cfg.SCREEN_WIDTH - cfg.PIPE_WIDTH - cfg.PIPE_SPACER:
            pipes.append(Pipes())


        # COLLISION DETECTION
        for i, bird in enumerate(birds):
            for pipe in pipes:
                if collision_detection(bird, pipe):
                    birds_alive[i] = False
                    break
            
        # DRAWING OBJECTS
        ## fill screen with background
        cfg.SCREEN.fill(cfg.BLUE)
        ## pipes
        for pipe in pipes:
            pipe.draw()
        ## birds. chinese_maal is to be killed
        chinese_maal = []
        for i, bird in enumerate(birds):        
            if birds_alive[i]:
                bird.draw()
            else:
                bird.color = cfg.RED
                bird.draw()
                chinese_maal.append(bird)
        ## these birds are bred out
        ## because CHINA!
        for bird in chinese_maal:
            networks.pop(birds.index(bird))
            genes.pop(birds.index(bird))
            birds.pop(birds.index(bird))

        # UPDATE SCREEN
        Borders.draw()
        pygame.display.update()

def algo(config_file):
    """
    - Setups the algorithm from the configuration file
    - Actiavtes the main game function for the number of generations 
    - prints out statistics for each gen
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # this is the object which controls the rest of objects
    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    # runs for 42 generations
    winner = pop.run(neat_play, 42)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == '__main__':
    # finding the file
    local = os.path.dirname(__file__)
    name = 'Algorithm/config-feedforward.txt'
    try:
        config_file = os.path.join(local, name)
    except:
        print(f"File './{name}' NOT found, terminating!")
    algo(config_file)