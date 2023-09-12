"""problem 1"""

input = [1, 10, 44, 12, 0, -1]

def findMax(input):
    max = 0    #initializing max value to zero first
    for e  in input:
        if e > max :
            max = e #if e is greater than max, reset max value

    print(max)

findMax(input)