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

def print_grid() :
    """
    Show the grid function, replace 0 with a dot

    """
    for row in range(SIZE) :
        for col in range(SIZE) :            
            if grid[row][col]==0 :
                print(".",end=" ")
            else :
                print(grid[row][col],end=" ")
        print()

def solve(n):
    if n==0:
        global t
        t = t + 1
        #print(f"The solution {t} :")
        #print("----------------") 
        print_grid()
        input(f"More?")
        return True

    for x in range(0,SIZE):
        for y in range(0,SIZE):
            #import pdb;pdb.set_trace()
            if grid[x][y] != 'Q' and isvalid(grid,x,y):
                grid[x][y] = 'Q' 
                #solve(n-1)
                if solve(n-1)==True:
                    return True
                solve(n-1)
                grid[x][y] = 0
            
    return False

#Initialize the solution number
t = 0

#Initialize the 8*8 array， You can adjust the array size by adjusting the parameter of size
SIZE = 4
grid = [[0]*SIZE for i in range(SIZE)]
row = 0
t = 0
# The entrance function
solve(4)

        
