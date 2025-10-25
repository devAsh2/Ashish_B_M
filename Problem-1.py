#Problem-1: Create a small calculator which performs operations such as Addition, 
# Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


# Note: Problem statement requires datatype of a and b in double but we have used
#       float because in python float does same job of double and there is no 
#       explicit double datatype
class Calculator:
    #initialize my object with starting variables
    def __init__(self,a:float, b:float,type:str):
        self.a=a 
        self.b=b 
        self.type=type.lower()
    
    def compute(self)->float:
        if self.type == 'add':
            return self.a+self.b
        elif self.type == 'subtract':
            return self.a-self.b
        elif self.type == 'multiplication':
            return self.a*self.b 
        elif self.type == 'division':
            return self.a/self.b
        else:
            raise  ValueError("Operation not available") 

# Input section
# calc = Calculator(10.5, 2.5, "Division")
# result = calc.compute()
# print("Result:", result) # output : 4.2

# calc = Calculator(10.5, 2.5, "add")
# result = calc.compute()
# print("Result:", result) # output : 13

# calc = Calculator(10.5, 2.5, "subtract")
# result = calc.compute()
# print("Result:", result) # output : 8

calc = Calculator(10.5, 2.5, "multiplication")
result = calc.compute()
print("Result:", result) # output : 26.25