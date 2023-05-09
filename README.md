# CSP-AI-Project
Link to the dataset : https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings/code?resource=download
This dataset contains 3 million Sudoku puzzles and their solutions. The level of difficulty varies -- some can be solved easily by a beginner, while others will challenge experienced solvers. Most puzzles have between 23 and 26 clues. The minimum number of clues in the dataset is 19, and the maximum is 31. It has been shown that 17 is the minimum number of clues for a valid, uniquely solvable Sudoku puzzle. However, these puzzles are difficult to find, so they are not included in our dataset.
The puzzles were generated using Blagovest Dachev's Sudoku generator and solver, at https://github.com/dachev/sudoku.

# Project Details
The goal of this project to collect few samples of easy and hard puzzles from the dataset and use multiple CSP algorithms to find the solution. The algorithms used are backtracking, forward jumping, Arc consistency-AC1 and AC3. The project presents comparative analysis of all the algorithms by comparing their time, number of iterations and space complexity of each algorithm taken to find the solution. 
Please read the final report for more details.

Note: The AC3 algorithm uses previously created functions for ease. Those functions can be accessed from the repo as 'UsedFunctions.zip'. While working on the notebook, the file was mounted and used. 

# References
1. https://www.kaggle.com/datasets/radcliffe/3-million-sudoku-puzzles-with-ratings?resource=download
2. https://www.kaggle.com/code/radcliffe/exploring-the-3m-sudoku-puzzle-dataset
3. https://www.geeksforgeeks.org/solve-sudoku-with-computer-vision-and-constraint-satisfaction-algorithm/#
4. https://www.geeksforgeeks.org/sudoku-backtracking-7/#
