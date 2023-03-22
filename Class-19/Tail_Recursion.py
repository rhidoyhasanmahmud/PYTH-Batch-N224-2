sum = 0 # Global Variable

def sum_tail_recursive(num):
    n = 10 #  Local Variable
    global sum # Sum - Global Variable

    if num == 0:
        return sum

    else:
        sum += num
        return sum_tail_recursive(num - 1)

print(sum)
print(sum_tail_recursive(5))
print(sum)
# num = 5 [ 1 + 2 + 3 + 4 + 5 ] - return
