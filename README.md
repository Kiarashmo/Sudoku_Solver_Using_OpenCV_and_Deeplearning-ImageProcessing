# Sudoku Solver with CNN and Backtracking Algorithm

This repository contains a Sudoku solver implemented using Convolutional Neural Networks (CNN) and the backtracking algorithm. The solver is built using the PyTorch framework. Sudoku is a popular number-placement puzzle that requires filling a 9x9 grid with digits while following certain rules.

The solver utilizes two main approaches:

1. **Convolutional Neural Networks (CNN):**
   - A CNN is trained to recognize digits in a 9x9 grid.
   - The trained model can extract the digits from an input Sudoku image or grid.
   - This approach helps in preprocessing and digit recognition.

2. **Backtracking Algorithm:**
   - After extracting the digits using the CNN, the solver employs the backtracking algorithm to solve the puzzle.
   - The backtracking algorithm is a recursive algorithm that explores all possible solutions and finds the correct one.
   - It efficiently handles the puzzle's constraints and reduces the solution space.

## Repository Structure

The repository is organized as follows:

- `model/`: Includes the trained CNN model for digit recognition.
- `notebooks`: Includes the model notebook and solver notebook.
- `test image`: Include one test image for testing the solver.

## Acknowledgments

- The CNN model architecture and training process were inspired by various online resources and tutorials.
- The backtracking algorithm implementation follows well-established techniques for solving Sudoku puzzles.

## Contributing

Contributions to this repository are welcome! If you have any improvements, bug fixes, or new features, feel free to submit a pull request.
