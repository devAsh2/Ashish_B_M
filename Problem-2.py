# Problem-2: With a single integer as the input, generate the following until a = x
#  [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......

def series(n:int):
    number = 1
    for i in range(n):
        print(number, end=", " if i<n-1 else "")
        number+=2

#series(1) #output : 1
#series(2) #output : 1, 3
#series(3) #output : 1, 3, 5
series(4) #output : 1, 3, 5, 7