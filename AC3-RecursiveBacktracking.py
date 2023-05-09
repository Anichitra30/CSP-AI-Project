# Arc Consistency
import sys
import os

py_file_location = "/content/drive/MyDrive/AI project"
sys.path.append(os.path.abspath(py_file_location))

from utils import generate_CSP, generate_assignment
from backtracking import recursive_backtracking
import copy


def conflicts(x, y):
    return x == y


def revise_sudoku(CSP, Xi, Xj):
    revised = False
    new_CSP = copy.deepcopy(CSP)

    for x in CSP.get("domains").get(Xi):
        broken = False

        for y in CSP.get("domains").get(Xj):
            if not conflicts(x, y):
                broken = True
                break

        if not broken:
            new_CSP.get("domains").get(Xi).remove(x)
            revised = True

    return revised, new_CSP


def arc_consistency(CSP, revise = revise_sudoku):
    queue = [(Xi, Xj) for Xi in CSP.get("variables") for Xj in CSP.get("neighbors").get(Xi)]

    while len(queue) != 0:
        Xi, Xj = queue.pop(0)

        revise_state, new_CSP = revise(CSP, Xi, Xj)
        if revise_state: # the domain of Xi has been changed
            if len(new_CSP.get("domains").get(Xi)) == 0:
                return False, new_CSP

            for xk in new_CSP.get("neighbors").get(Xi):
                if xk != Xj:
                    queue.append((xk, Xi))

            CSP = new_CSP

    return True, CSP


def solve(grid_string, multipleSolutions = False):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)
    solutions = []

    is_arc_consistent, new_csp = arc_consistency(CSP)

    if (is_arc_consistent):
        recursive_backtracking(assignment, new_csp, solutions, multipleSolutions)

    return solutions, new_csp

  
  def ConvertIntoString(puzzle):

  stringConvert=""""""
  for i in puzzle:
    for x,j in enumerate(i):
      stringConvert+=str(j)+" "
      #print(x)
      if(x==8):
        stringConvert+="\n"
  #print(stringConvert)
  return stringConvert

from utils import generate_sudoku_string
def printSolutions(solutions, CSP):
    if len(solutions) == 0:
        print("No solution found\n")
    else:
        for solution in solutions:
            print(generate_sudoku_string(solution, CSP))
            print()


stringConvert=""""""
puzzle = [    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 5, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in puzzle:
  for x,j in enumerate(i):
    stringConvert+=str(j)+" "
    #print(x)
    if(x==8):
      stringConvert+="\n"
print(stringConvert)

grid_string = """
    5 3 0 0 7 0 0 0 0
    6 0 0 1 9 5 0 0 0
    0 9 8 0 0 0 0 6 0
    8 0 0 0 6 0 0 0 3
    4 0 0 8 0 3 0 0 1
    7 0 0 0 2 0 0 0 6
    0 6 0 0 0 0 2 8 0
    0 0 0 4 1 9 0 0 5
    0 0 0 0 8 0 0 7 9
    """
print("arc consistency\n")
#printSolutions(*solve(stringConvert))

# for easy puzzles
import time
from utils import generate_sudoku_string

def printSolutions(solutions, CSP):
    if len(solutions) == 0:
        print("No solution found\n")
    else:
        for solution in solutions:
            print(generate_sudoku_string(solution, CSP))
            print()


# Now using the dataset for hard, do backTracking
#Please note that the number of iterations is calculated as every move taken to fill each cell
timeVE=[]
x=0
for puzzle in easy:
  # covert the inputs into the valid strings
  stringConvert=""""""
  for i in puzzle:
    for x,j in enumerate(i):
      stringConvert+=str(j)+" "
      #print(x)
      if(x==8):
        stringConvert+="\n"
  print(stringConvert)
  # Solve the puzzle with the start and the end time
  start_time = time.time()
  printSolutions(*solve(stringConvert))
  end_time = time.time()
  timeVE.append(round(end_time - start_time,6))
  #print("Time taken:",timeVE[x] , "seconds")
  #printFwdIteration()

print(timeVE)


# for hard
import time
from utils import generate_sudoku_string

def printSolutions(solutions, CSP):
    if len(solutions) == 0:
        print("No solution found\n")
    else:
        for solution in solutions:
            print(generate_sudoku_string(solution, CSP))
            print()


# Now using the dataset for hard, do backTracking
#Please note that the number of iterations is calculated as every move taken to fill each cell
timeVH=[]
x=0
for puzzle in hard:
  # covert the inputs into the valid strings
  stringConvert=""""""
  for i in puzzle:
    for x,j in enumerate(i):
      stringConvert+=str(j)+" "
      #print(x)
      if(x==8):
        stringConvert+="\n"
  print(stringConvert)
  # Solve the puzzle with the start and the end time
  start_time = time.time()
  printSolutions(*solve(stringConvert))
  end_time = time.time()
  timeVH.append(round(end_time - start_time,6))
  #print("Time taken:",timeVH[x] , "seconds")
  #printFwdIteration()

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
