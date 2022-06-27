# Flapi Bird
**Implementing the legendary, Flappy Bird using the NEAT(Neuroevolution of augmenting topologies) algorithm.**

## Requirements:

Execute the following command for the dependencies

`pip install -r requirements.txt`

This installs: `neat-python` and `pygame` using `pip`

## The Game:
- Run the main.sh script

- There are two options to Play the game: 
    - Play the game yourself
    - Let the NEAT Algorithm play it for you

## The Algorithm:
NEAT is a genetic algorithm, which evolves different structures for the neural network. There are some initial species, and those who live the longest have the highest score. Thus passing on their "genes", which is basically their network. Some mutations and and some cross-overs create the Next-Gen NN.

These networks start out simple, and for a game such as this, do not require many generations to get god-level at it. (Of course, given enough population size to begin with.)

## Configuration:
- Two Config files exist; one for the game settings and another one for the algorithm. 

- Changing the variables in the game config file changes the look and play of the game. This happens for both the cases: Whether you play or the algo plays it.

- Changin the variables in the `./Game/Algorithm/config-feedforward.txt` file changes the specifics of the way the algo works.

- Inside of NEATplay.py, there are a couple of parameters that are fed into the NN. For more robust experimentation, you can change them.
Note: Make sure the number of input parameters are reflected in both the play file and the config file.

### References
- [The NEAT Algorithm Paper](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)
- The implementation of the NEAT algorithm is taken from [here](https://github.com/CodeReclaimers/neat-python) 
