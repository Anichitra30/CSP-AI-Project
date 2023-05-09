# forward jumping main
ForwardIterartion=0
def solve_sudoku(puzzle):
    global ForwardIterartion
    ForwardIterartion=0
    # Define a function to get the possible values for an empty cell
    def get_possible_values(row, col):
        # Create a set of all possible values
        possible_values = set(range(1, 10))
        # Remove values that conflict with the row and column
        for i in range(9):
            possible_values.discard(puzzle[row][i])
            possible_values.discard(puzzle[i][col])
        # Remove values that conflict with the 3x3 subgrid
        subrow = (row // 3) * 3
        subcol = (col // 3) * 3
        for i in range(subrow, subrow + 3):
            for j in range(subcol, subcol + 3):
                possible_values.discard(puzzle[i][j])
        # Return the set of possible values
        return possible_values

    # Define a function to perform forward jumping
    def forward_jumping():
        # Find the next empty cell with the fewest possible values
        min_values = 10
        new_val=0
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    values = get_possible_values(row, col)
                    if min_values > len(values):
                        min_values = len(values)
                        min_row, min_col,new_val= row, col,values
        # If there are no empty cells, the puzzle is solved
        if min_values == 10:
            return True
        # Try each possible value for the cell
        
        for value in new_val:
            global ForwardIterartion
            ForwardIterartion+=1
            #print(ForwardIterartion)
            puzzle[min_row][min_col] = value

            # Check if the puzzle can be solved from here
            if forward_jumping():
                return True
            # If not, backtrack and try the next value
            ForwardIterartion+=1
            puzzle[min_row][min_col] = 0

        # If no solution found, return False
        return False

    # Call the forward jumping function and return the solved puzzle
    forward_jumping()
    return puzzle

def printFwdIteration():
  global ForwardIterartion
  print("Numbe of Forward Interations  = ",ForwardIterartion)
  #ForwardIterartion=0


  #solve_sudoku(convertPuzzleFormat(df.puzzle[5]))
print(convertPuzzleFormat(df.puzzle[5]))
print(easy[0])
#printFwdIteration()

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
  #printIterationBT()

print(timeVE)

import time
# Now using the dataset for hard, do backTracking
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
  #printIterationBT()

print(timeVH)

#to visualize time taken 
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
