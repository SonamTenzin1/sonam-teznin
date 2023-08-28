def find_max(input):
    max =  0  
    for e in input:
        if e > max :
            max = e

    print(max)

input = [7,3,4,5,28]
find_max(input)