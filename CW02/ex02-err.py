
"""
Author: Mengjiao ZHAO
Date: 10/23/2021

The guessing game
It is a Python program that plays the number guessing game. The user thinks of a number within a given interval (e.g. [1, 100],
including both extremes of the interval), but does not input anything to the program; Program should ask questions to the user 
to know whether the number is less than, equal or greater than another number.
"""
def Game():
    # Assuming that given Interval 1 to 100
    arry = list(range(1,101))
    #start index
    start = 0
    #length of the list
    end = len(arry)
    #guess the number of executions
    count = 0
    while start <= end:
        mid = (start + end ) //2
        print(f"Is your number greater (>), equal (=), or less (<) than {mid}?")
        item = input("please input '>' '<' or '=' !    ")
        if item == "=":
            count += 1
            print(f"I have guessed it!\n I needed {count} steps!")
            return True           
        elif item == "<":
            count += 1
            end = mid -1
        elif item == ">":
            count += 1
            start = mid +1
        else:
            print("Input error, please input '>' '<' or '='")
            continue
    print("Cutie, you need to think of a round number between 1 and 100～")

Game()
