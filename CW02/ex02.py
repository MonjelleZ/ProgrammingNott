
"""
Author: Mengjiao ZHAO
Date: 11/8/2021

The guessing game
It is a Python program that plays the number guessing game. The user thinks of a number within a given interval (e.g. [1, 100],
including both extremes of the interval), but does not input anything to the program; Program should ask questions to the user 
to know whether the number is less than, equal or greater than another number.
"""

def Search(arry):   
    count = 0 # Initializes calculate times
    start, end = 0, len(arry)-1 #Initializes the index of the first and last element
    print(f'Please think of a number between {arry[0]} and {arry[len(arry)-1]}!')
    while start <= end:
        mid_index = (start + end) // 2 # index of the middle element
        print(f"Is your number greater (>), equal (=), or less (<) than {arry[mid_index]}?")
        item = input("please input '>' '<' or '=' !    ")       
        if item == "=": # indicates that the guess is correct  
            count += 1 
            print(f"I have guessed it!\n I needed {count} steps!")
            return True
        elif item == "<": 
            count += 1
            end = mid_index - 1
        elif item == ">":
            count += 1
            start = mid_index + 1
        else:
            print("input error, please reinput correct string")
            continue
    
    print("You are a lier! Exit the program.")

if __name__ == '__main__':
    arry = list(range(1,101)) # given interval [1, 100]
    Search(arry)