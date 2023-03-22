# Recursion

"""
- Recursion is a programming technique in which a *function* calls itself one or more times to solve a problem.
- Two Parts: 1. Base Case and 2. Recursive case

- A loop is control structure that iteratively executes a block of code until a certain condition is met.
- Recursion, is a technique in which a function calls itself to solve a problem.

- Recursion can be less efficient than loop
-
"""

"""

for cnt in range(countDown):
    print("Hello World!")
"""
"""
countDown = int(input())
def countDownString(cnt):  # 3
    # Base Case
    if cnt == 0:
        pass
    # Recursive case
    else:
        print("Hello World!")
        countDownString(cnt - 1)

# Function Call
countDownString(countDown)
"""
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n-1) # 4 / 3/ 2/ 1 / 0
    print(n)

head_recursion(10)

# Graph Algorithm / Tree Algorigm