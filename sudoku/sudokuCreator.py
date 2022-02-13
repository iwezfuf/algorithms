# Jan 2021

import random

def sudoku_generator_solver():
 
 def sudoku_oknotok(sudoku):
  for i in range(9):
   section = []
   section.extend([*sudoku[i][0],*sudoku[i][1],*sudoku[i][2]])
   if 0 in section:
    if len(set(section)) != 10 - section.count(0):
     return False
   elif len(set(section)) != 9:
    return False

  for i in range(9):
   row = []
   for j in range(3):
    row.extend(sudoku[i//3*3+j][i%3])
   if 0 in row:
    if len(set(row)) != 10 - row.count(0):
     return False
   elif len(set(row)) != 9:
    return False

  for i in range(9):
   col = []
   for j in range(3):
    for k in range(3):
     col.append(sudoku[i//3+3*j][k][i%3])
   if 0 in col:
    if len(set(col)) != 10 - col.count(0):
     return False
   elif len(set(col)) != 9:
    return False
   
  return True

 def sudoku_create():
  sudoku = [[[0,0,0] for j in range(3)] for i in range(9)]
  return sudoku
  
 i = 0
 def sudoku_solve(sudoku,i):
  flatsudoku = [i for j in sudoku for i in j]
  flatsudoku = [i for j in flatsudoku for i in j]  
  if 0 not in flatsudoku:
   for i in range(9):
    row = []
    for j in range(3):
     row.extend(sudoku[i//3*3+j][i%3])
    print(*row)
   quit()
   return sudoku
  lst = list(range(1,10))
  random.shuffle(lst)
  for new in lst:
   sudoku[i//9][i//3%3][i%3] = new
   if sudoku_oknotok(sudoku):
    sudoku_solve(sudoku,i+1)
   else: sudoku[i//9][i//3%3][i%3] = 0
 
 sudoku_solve(sudoku_create(), i)
  
  
print(sudoku_generator_solver())
