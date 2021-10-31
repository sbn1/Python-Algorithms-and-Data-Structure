# -*- coding: utf-8 -*-
"""
There is a gold mine of nxm dimensions. 
Each field in this mine contains a positive integer which is 
the amount of gold in tons. Initially the miner is at first
column but can be at any row. He can move only: right, right up or 
right down, from a given cell. Find out maximum amount of gold he
 can collect.The allowed movements are right-up, right-down, right.
 
 
"""

def gold_matrix(arr):
    
     n = len(arr)
     m = len(arr[0])
     # An empty matrix that will store the values
     dynamic_matrix =[[0 for i in range(n)] for j in range(m)]
     
     # the search will srtart from last coloumn and move backwards to column zero
     for col in range(m-1,-1,-1):
         for row in range(n):
             # from the last coloumn there are not movements to right
             if (col == m-1):
                 right = 0
             else:
                right = dynamic_matrix[row][col + 1]
             #from first row and last coloumn there are not right and up movements
             if (row == 0 or col == m-1 ):
                 right_up = 0
             else:
                 right_up = dynamic_matrix[row - 1][col + 1]
             #from last row and last coloumn there are no right down movements 
             if (row == n-1 or col == m-1):
                 right_down = 0
             else:
                 right_down = dynamic_matrix[row + 1][col + 1]
             #print(right_down)
             # the dynamic matrix take the value from the mine matrix + the maximum movement(right, right_up, right_down)
             dynamic_matrix[row][col] = arr[row][col] + max(right, right_down,right_up)
        #the maximum value from the column 0 is the maximum amount of gold   
        max_value = max([dynamic_matrix[i][0] for i in range(n)])
              
     return max_value



mine1 =[[1, 3, 3],
        [2, 1, 4],
        [0, 6, 4]]

mine2 = [[1, 3, 1, 5],
         [2, 2, 4, 1],
         [5, 0, 2, 3],
         [0, 6, 1, 2]]

print(gold_matrix(mine1))
print(gold_matrix(mine2))
