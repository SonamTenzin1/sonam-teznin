"""problem 1"""
def check(lst):
    count_19 = lst.count(19)
    count_5 = lst.count(5)
    
    return count_19 == 2 and count_5 >= 3
#count_19 == 2 checks if there are exactly two occurrences of 19 and if there are at least three occurrences of 5.

input1 = [19, 19, 15, 5, 3, 5, 5, 2]
input2 = [19, 15, 15, 5, 3, 3, 5, 2]
input3 = [19, 19, 5, 5, 5, 5, 5]

output1 = check(input1)
output2 = check(input2)
output3 = check(input3)

print(output1)  
print(output2)  
print(output3)  

"""problem 2"""
def stone_piles(n):
    return [n + 2 * i for i in range(n)]

input1 = 2
input2 = 10
input3 = 3
input4 = 17

output1 = stone_piles(input1)
output2 = stone_piles(input2)
output3 = stone_piles(input3)
output4 = stone_piles(input4)

print(output1)  
print(output2)  
print(output3)  
print(output4) 
