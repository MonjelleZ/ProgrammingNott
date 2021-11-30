
def possible(y,x,n):
    # check all the 9 positions in square
    for i in range(0,SIZE) :
        for j in range(0,SIZE) :
            if grid[i][j]==n :
                return False
    # checked everything, it is possible
    return True

def print_grid(x) :
    for row in range(SIZE) :
        print(x*3*" ",end="")
        for col in range(SIZE) :            
            if grid[row][col]==0 :
                print(".",end=" ")
            else :
                print(grid[row][col],end=" ")      
        print()



def solve(x) :
    """
    This version of the solve function contains lots of print statements 
    to help understand backtracking (including indentation based on the value of `x`)
    x: level in the recursion

    """
    print(f"{x*3*' '}solve({x}):")
    print_grid(x)
    input(f"{x*3*' '}----")
    # looking for an empty space
    for i in range(0,SIZE) :
        for j in range(0,SIZE) :
            if grid[i][j] == 0 :
                # we found an empty square, we need to try all digits from 1-9
                for n in range(1,10) :
                    if possible(i,j,n) :
                        # we can put n into that square
                        grid[i][j] = n
                        # recursively solve a smaller instance of the sudoku
                        solve(x+1)                        
                        # add comment
                        grid[i][j] = 0
                        print(f"{x*3*' '}Backtracking!") 
                        print(f"{x*3*' '}solve({x}):")
                        print_grid(x)
                        input(f"{x*3*' '}----")
                # we reached a dead end, backtrack 
                return
    # Problem solved! we got a full grid
    print(f"{x*3*' '}Solution: ")
    print_grid(x)
    # add comment
    input(f"{x*3*' '}More?")


SIZE = 3


grid=[[1,2,3],
     [4,5,6],
     [0,0,0]]
     
solve(0)
