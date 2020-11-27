# Ecosystem simulation Using Python

This is a basic simulation of an ecosystem using Python

## Simulation attributes

### Animals
**See Animal.py file**

Animals are the focus of the simulation. They move in order to eat food, survive, and reproduce


#### Attributes
Here are all the attributes of the animals in the simulation:
- Range (How far away can an animal see food)
- Speed (How many spaces an animal can move in one turn)
- Hunger (How much energy an animal has, once this hits zero the animal dies)

#### Movement
**See find_food, find_best_path, and move_to_food functions in Animal.py file**

The animal goes through a number of steps before it makes a move

- Find nearby food
- Create a path to the nearest food (Using the Breadth First Search algorithm)
- Move to the food turn by turn until it reaches the food

#### Eating and Reproducing
**See eat and reproduce functions in Animal.py file**

Each turn the animal checks if it has reached food, if it has it eats it.
- The animal gains energy from eating food (Amount corresponding to the food type)
- If the animals hunger attribute is greater than 19, two new animals are created that inherit the animals attribute unless a mutation occurs
  - The animals hunger attribute is also cut in half after reproducing

### Food
**See Food.py file**

The food in the simulation is the other main attribute, it is stationary and animals eat it to survive

#### Attributes
- X and Y coordinates (Position in the simulation)
- Type (How much energy the food gives the animal)

## Running the simulation
To run the simulation run *python Sim.py* in the command prompt.

By default, the simulation starts with 20 animals and repeats for 200 cycles.

To change this go to the bottom of the Sim.py file and change the arguments when initializing the sim class. The first argument is the initial number of animals, the second is the number of cycles the simulation will repeat for

After the simulation is complete, the data from the simulation will be written to the data.json file

**NOTE: Running the Sim.py file will rewrite the data.json file and previous data will be lost**

## Graphing the simulation
**See Graphs.py file**

Graphs are generated using matplotlib

To graph the simulation, run *python Graphs.py* in the command prompt

This will generate 2 graphs using simulation data from the data.json file. One of the overall population over the simulation and one of the attributes of the animals over the simulation. These can be viewed in the population.png file and the animals.gif file

All graphing is handled in the Graphs.py file

The plot_population function creates the population graph and the plot_animal_attributes function plots the animal attributes

## Simulation Display
**See Display.py file**

Display is created using pygame

To create a GUI of the simulation, run *python Display.py* in the command prompt

The will create a simple user interface that shows the animals represented as red squares and the food represented as blue squares  

## Queue Class
**See Queue.py**

The queue object is used in the Breadth First Search to find the animal's best path to food
It is a list like data structure, where data is added at the start and removed at the back
