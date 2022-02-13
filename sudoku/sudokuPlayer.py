# Jan 2021

import random

def sudoku_generator(num):
 
 sudoku = [[0 for i in range(9)] for i in range(9)]
 
 def check_sudoku(sudoku, position, newnum):
  if newnum in sudoku[position[0]]:
          return False
  for row in sudoku:
      if newnum == row[position[1]]:
          return False
  for i in range(3):
      for j in range(3):
          if newnum == sudoku[position[0]//3*3+i][position[1]//3*3+j]:
              return False
  return True

 def sudoku_fill(sudoku,position):
  flatsudoku = [i for j in sudoku for i in j]
  if 0 not in flatsudoku:
    sudoku_player(sudoku_ready(sudoku))
    return True
  newnums = list(range(1,10))
  random.shuffle(newnums)
  for num in newnums:
      if check_sudoku(sudoku,[position//9,position%9],num):
          sudoku[position//9][position%9] = num
          if sudoku_fill(sudoku,position+1):
              return True
  else: 
      sudoku[position//9][position%9] = 0
      return False

 def sudoku_ready(sudoku):
    counter = 0
    while counter != 81-num:
        position = random.randint(0,80)
        if sudoku[position//9][position%9]:
            sudoku[position//9][position%9] = 0
            counter += 1
    return sudoku

 def sudoku_player(sudoku):
     print("Example input: 5 8 6")
     print("This means put a 5 on box in row 8 in col 6")
     done = False
     nono = []
     for i in range(9):
         for j in range(9):
             if sudoku[i][j] != 0:
                 nono.append([i,j])
     while not done:
         try:
            print("Col:   ",* list(range(1,10)),sep="   ")
            for i in range(1,10):
                 if (i-1) % 3 == 0:
                     print("-"*43)
                 print("Row:", i, "   ",end="")
                 print(*sudoku[i-1],sep=" | ")
            flatsudoku = [i for j in sudoku for i in j]
            if 0 not in flatsudoku:
                 print("Wtf you actually did it")
                 done = True
            move = [int(i) for i in input().split(" ")]
            if [move[1]-1, move[2]-1] not in nono:
                sudoku[int(move[1])-1][int(move[2])-1] = int(move[0])
            else: print("Lol you thought. No cheating dumbass.")
         except:
             print("Bad input dummy.")
         print()

 sudoku_fill(sudoku,0)

print("Choose how many numbers you wanna start with (0-81)")
sudoku_generator(int(input()))
