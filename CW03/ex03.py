#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri 12

@author: Mengjiao ZHAO

"""

def print_grid() :
    """
    Show the grid function, replace 0 with a dot

    """
    for row in range(l) :
        for col in range(l) :            
            if grid[row][col]==0 :
                print(".",end=" ")
            else :
                print(grid[row][col],end=" ")
        print()

def isvalid(grid,row,col):
    """
    check if rows, columns, and diagonal have queens
    diagonal check function : |j - col | == |i - row|

    """
    n = len(grid)
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'Q':
                # check row ,colums and diagonal if have Queens, if have ,return false
                if i == row or j == col or j-col == i-row or j-col == - ( i - row ): 
                    return False
    return True

def solve(n):
    """

    n : Current row number, also can be seen as the number of put queens.

    """
    # If it is the last queen, print grid
    if n == l:
        global t
        t = t + 1
        print(f"The solution {t} :")
        print("----------------") 
        print_grid()
        input(f"More?")

    # looking for an empty space
    for y in range(0,l):
        # check if the empty space can be put a Queen
        if isvalid(grid,n,y):   
            grid[n][y] = 'Q' # Place a Queen
            if solve(n+1) == True: # if the next Queen can be put, return True
                return True
            else: # else backtracking
                grid[n][y] = 0 # Backtracking
    return False


#Initialize the solution number
t = 0

#Initialize the 8*8 array， You can adjust the array size by adjusting the parameter of l
l = 8
grid = [[0]*l for i in range(l)]

# The entrance function
solve(0)