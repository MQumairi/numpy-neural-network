# IN3063-coursework
Coursework for "IN3063 Programming and Mathematics in AI" by Mohammed Alqumairi (Mohammed.Alqumairi@city.ac.uk)

# Read Me
Code will be contained in src folder. In turn, the src folder holds five items:
- "data" folder
- "util.py" file
- "Task 1.ipynb" file
- "Task 2.ipynb" file
- "Task 3.ipynb" file

## data
A folder named "data". This holds the MNIST dataset, downloaded by PyTorch's torchivsion. If this folder does not exist in this directory when Tasks 2 or 3 are run, the MNIST dataset will download the data.

## util.py
This contains various utility functions used in Tasks 2 and 3. Mainly Used for preprocessing purposes. A description of what each function does, is provided as a comment above each function in util.py

## Task 1.ipynb
My solution to Task 1. Detailed instructions provided in the file. You should be able to run all cells in the Jupyter Notebook from start to finish, and it will process in a few seconds.

For instructions on how to play the game using an agent, scroll down to cell titled "Tutorial on Playing the Game Using An Agent". Make sure you have run all cells above this point, as well as the cell contaiing the class defining the agent you wish to play with.

WARNING: the Ant_Agent may take some time to process when playing a game with a large grid, and/or a game with many ants/batches.

## Task 2.ipynb
My solution to Task 2. Detailed instructions provided in the file. I reccomend reading through the Jupyter Notebook, and only running cells on a one-by-one basis as needed.

WARNING: running all cells in the Jupyter Notebook from top to bottom may take a long time to process, as this would involve training multiple neural networks.

To skip to how to use the numpy neural network, scroll down to the cell titled "Tutorial Building and Training our Numpy Neural Network", and read from there. Make sure you have run all the code cells above this cell.

## Task 3.ipynb
My solution to Task 3. Detailed instructions provided in the file. I reccomend reading through the Jupyter Notebook, and only running cells on a one-by-one basis as needed.

WARNING: running all cells in the Jupyter Notebook from top to bottom may take a long time to process, as this would involve training multiple neural networks.

To skip to how to use the pytorch neural network, scroll down to the cell titled "Tutorial On Using the PyTorch Neural Network (PT_NN)", and read from there. Make sure you have run all the code cells above this cell.
