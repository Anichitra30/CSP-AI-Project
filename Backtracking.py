#to download the dataset
#https://www.kaggle.com/code/radcliffe/exploring-the-3m-sudoku-puzzle-dataset/notebook
import numpy as np 
import pandas as pd
path = '/content/drive/MyDrive/sudoku-3m.csv'
df = pd.read_csv(path)
df.head()


#format of first puzzle
def view_grid(puzzle_string):
    return pd.DataFrame(np.array(list(puzzle_string.replace('.', ' '))).reshape((9, 9)))

view_grid(df.puzzle[0]) 

# To convert the input string from the .csv file into the usable format used by our code.
def convertPuzzleFormat(s):
  puzzle=list()
  temp=[]
  for i,j in enumerate(s):
    i+=1
    if(i%9!=0):
      if(j=='.'):
        temp.append(0)
      else:
        temp.append(int(j))
    else:
      if(j=='.'):
        temp.append(0)
      else:
        temp.append(int(j))
      puzzle.append(temp)
      temp=[]   
  return puzzle 
  #print(puzzle)
#print(convertPuzzleFormat(df.puzzle[0]))

# Make two lists easy and hard for the Sudoku puzzles which will store 1-4 level as easy  and 6-8 level as hard from the file read above
# and the stored format will be after converting the convertPuzzleFormat
easy=[]
hard=[]
def Seperation():
  for i,j in enumerate(df.difficulty):
    if(j>=1 and j<=4 and len(easy)<=9):
      easy.append(convertPuzzleFormat(df.puzzle[i]))
    elif(j>=6 and j<=8 and len(hard)<=9):
      hard.append(convertPuzzleFormat(df.puzzle[i]))

#print(easy)
Seperation()
# For Visualization creating a couple of dictionaries

print(len(easy))
print(len(hard))
print(easy[0])

#backtracking 
BTIteration=0
def solve_sudoku(grid):
    """
    Solves a Sudoku puzzle using backtracking.

    :param grid: A list of lists representing the Sudoku grid.
    :return: True if the Sudoku puzzle is solved, False otherwise.
    """
    global BTIteration
    # Find the next empty cell in the grid
    row, col = find_empty_cell(grid)

    # If all cells are filled, the puzzle is solved
    if row is None:
        return grid

    # Try all possible values for the empty cell
    for value in range(1, 10):
        if is_valid(grid, row, col, value):
            # If the value is valid, add it to the grid
            BTIteration+=1
            grid[row][col] = value

            # Recursively try to solve the puzzle
            if solve_sudoku(grid):
                return grid

            # If the puzzle can't be solved with the current value, backtrack
            BTIteration+=1
            grid[row][col] = 0
            

    # If no value works, the puzzle can't be solved
    return False


def find_empty_cell(grid):
    """
    Finds the next empty cell in the grid.

    :param grid: A list of lists representing the Sudoku grid.
    :return: A tuple representing the row and column indices of the next empty cell, or (None, None) if there are no empty cells.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None


def is_valid(grid, row, col, value):
    """
    Checks if the given value is valid for the cell at the given row and column indices.

    :param grid: A list of lists representing the Sudoku grid.
    :param row: An integer representing the row index.
    :param col: An integer representing the column index.
    :param value: An integer representing the value to check.
    :return: True if the value is valid, False otherwise.
    """
    # Check if the value is already in the row
    if value in grid[row]:
        return False

    # Check if the value is already in the column
    if value in [grid[i][col] for i in range(9)]:
        return False

    # Check if the value is already in the 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    if value in [grid[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]:
        return False

    # If the value is not already in the row, column, or box, it is valid
    return True


# This is to print the nmber of Iterations
def printIterationBT():
  print("The number of Iterations for BackTracking= ",BTIteration)


  import time
# Now using the dataset for easy , do backTracking
#Please note that the number of iterations is calculated as every move taken to fill each cell
timeVE=[]
x=0
for i in easy:
  # Solve the puzzle with the start and the end time
  start_time = time.time()
  solution = solve_sudoku(i)
  end_time = time.time()

  # Print the solution
  print("\n\nFor Easy Solution\n")
  if solution:
      for row in solution:
          print(row)
  else:
      print("No solution found.")
      # printing the time
  timeVE.append(round(end_time - start_time,6))
  print("Time taken:",timeVE[x] , "seconds")
  x+=1
  printIterationBT()
print(timeVE)

import time
# Now using the dataset for hard , do backTracking
#Please note that the number of iterations is calculated as every move taken to fill each cell
timeVH=[]
x=0
for i in hard:
  # Solve the puzzle with the start and the end time
  start_time = time.time()
  solution = solve_sudoku(i)
  end_time = time.time()

  # Print the solution
  print("\n\nFor Hard Solution\n")
  if solution:
      for row in solution:
          print(row)
  else:
      print("No solution found.")
      # printing the time
  timeVH.append(round(end_time - start_time,6))
  print("Time taken:",timeVH[x] , "seconds")
  x+=1
  printIterationBT()

print(timeVH)


from matplotlib import pyplot as plt
import numpy 
def VisualizeTime(timeV,color):
  bins=[] 
  for i in range(1,11):
    bins.append(i)

  print(len(bins))

  plt.bar(bins, timeV,color=color)
  plt.title('Time Visualization')
  plt.xlabel('Puzzles')
  plt.ylabel('Time (sec)')
  plt.show()


VisualizeTime(timeVE,'blue')
VisualizeTime(timeVH,'red')
