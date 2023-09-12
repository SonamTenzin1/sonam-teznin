input = [1, 10, 44, 12, 0, -1]

def findMax(input):
    if len(input) == 0:
        print('The input array is empty.')
        return

    result_max = input[0]  # Initialize the result_max with the first element of the array

    for num in input:
        if num > result_max:
            result_max = num  # Update result_max if a larger number is found

    print('The maximum of the input is:', result_max)

findMax(input)
