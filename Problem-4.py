# Problem-4: Get the total count of number listed in the dictionary which is 
# multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

# Problem statement: counting how many numbers in a list are divisible by each digit
#                    from 1 to 9.

# algorithm
# keep i pointer on start of [1,2,3,4,5,6,7,8,9]
# keep j pointer on start of input : [1,2,8,9,12,46,76,82,15,20,30]
# for each element at i, check if j has an element which is a multiple
#  yes if increment ith value+=1 else move on
# store in hashmap i.e {} in python


from typing import List
def count_multiple(input:List[int])->dict:
    result = {}
    multiple = [1,2,3,4,5,6,7,8,9]
    result = {i: 0 for i in range(1, 10)}  # initialize keys 1–9 with 0
    for i in range(len(multiple)):
        for j in range(len(input)):
            if input[j] % multiple[i] == 0:
                number = multiple[i]
                result[number] +=1
    return result

# input section
input = [1,2,8,9,12,46,76,82,15,20,30]
result = count_multiple(input)
print("Result: ", result)

#Output :
# Result:  {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}