"""problem 1"""

input = [1, 10, 44, 12, 0, -1]

def findMax(input):
    max = 0    #initializing max value to zero first
    for e  in input:
        if e > max :
            max = e #if e is greater than max, reset max value

    print(max)

findMax(input)

"""problem 2"""

input_string = "(((((((((())"

def findFloorAtEnd(input_string):
    floor_at_end = 0

    for bracket in input_string:
        if bracket == '(':
            floor_at_end += 1  # Go up one floor for an open bracket
        elif bracket == ')':
            floor_at_end -= 1  # Go down one floor for a close bracket

    print('At the end, you will be at floor number:', floor_at_end)

findFloorAtEnd(input_string)
