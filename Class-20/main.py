"""
1. Lambda functions in Python
2. Comprehensions in Python
"""

""" 

- Normal Function 

def functionName(Parameters):
    // statements - 1
    // statements - 2
    // statements - 3 
    
- Lambda Function 

    - Anonymous Function/Unnamed Function 
    - lambda keyword  
    - Single Statement 




# Normal Function
def add100WithTheArgument(num):
    return num + 100


print(add100WithTheArgument(10))

# Lambda Function Syntax - lambda arguments : expression

add = lambda num: num + 100

print(add)  # <function <lambda> at 0x000002D4E4CAE700>
print(add(10))  # 110

lst = [34, 12, 64, 55, 75, 13, 63]

# filter(function, iterable)

odd_list = filter(lambda num: num % 2 == 1, lst)
print(odd_list) # <filter object at 0x0000023EBBB2FFD0>
print(list(odd_list))

def is_odd(num):
    return num % 2 == 0

even_list = filter(is_odd, lst)
print(list(even_list))
"""
# map

lst = [1, 2, 3, 4, 5]


def sqrValue(value):
    return value ** 2


sqr_lst = map(lambda value: value + 2, lst)
print(sqr_lst)  # <map object at 0x0000021B1EEFFAC0>
print(list(sqr_lst))
print(lst)

sqr_lst_conditional_logic = map(lambda value: value + 10 if value % 2 == 0 else value + 5, lst)
print(list(sqr_lst_conditional_logic))

