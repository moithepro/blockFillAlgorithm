# Game Puzzle Solver

This is a simple project designed to illustrate how seemingly complex game puzzles can be solved using straightforward algorithms. The goal is to teach and demonstrate how simple techniques, such as finding a Hamiltonian path, can provide solutions to puzzles that initially appear daunting.

## Inspiration

This project was inspired as the solution to a puzzle game available on Google Play. You can check out the game [here](https://play.google.com/store/apps/details?id=com.playfun.games.blockfill.oneline.connect.puzzle&pli=1).

## Description

The project focuses on finding Hamiltonian paths in a given grid. A Hamiltonian path is a route that visits every cell exactly once without revisiting any cell. The grid may have obstacles, a start position, and empty cells that need to be traversed.

The code included in this repository is structured to make the logic easy to follow for anyone interested in algorithms, game theory, or learning how to approach seemingly complicated problems with simple solutions.

### Main Files

- **HamiltonPath.py**: Contains the core function that finds the Hamiltonian path in a grid, taking into account roadblocks, valid moves, and traversal logic.
- **main.py**: The entry point of the project. It reads a grid configuration from a text file, finds the Hamiltonian path, and prints the solution to the console.
- **utils.py**: Provides utility functions, including reading the grid from a file, printing the grid with colored symbols to represent different cell types, and displaying the path using arrows for clarity.

### How to Use

1. Prepare a text file representing the grid configuration. Different values represent different cell types:
   - `0`: Empty cell
   - `1`: Roadblock
   - `2`: Starting position
2. Run the `main.py` script to see the printed path found by the algorithm. The grid, along with the Hamiltonian path, will be displayed in a color-coded format for easy understanding.

### Example

A sample grid configuration might look like this:

```
2 0 1 0
0 0 1 0
0 0 0 0
```

Running the `main.py` script with this grid will print the Hamiltonian path that starts from the `2` and visits all reachable cells, avoiding the roadblocks (`1`).

### Dependencies

- Python 3.x

No additional external libraries are required to run this project.

### Running the Project

```
python main.py
```

Make sure to modify the `file` variable in `main.py` to point to your grid configuration text file.

## Purpose

The project is a learning exercise meant to show that game puzzles that look complicated can often be solved with well-defined, simple algorithms. It aims to demystify problem-solving by breaking down the complexity into simple, manageable steps.

Feel free to explore, modify, and expand upon this code to further understand the Hamiltonian path and other similar algorithms!

