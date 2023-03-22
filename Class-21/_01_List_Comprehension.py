lst = [1, 2, 3, 4, 5]

# List Comprehension

lst_comp = [num for num in range(1, 6)]

print(lst_comp)

even_lst_comp = list(num for num in range(900, 1001, 50) if num % 2 == 0)

print(even_lst_comp)

lst = []
for num in range(1, 1000):
    if num % 2 == 0:
        lst.append(num)

print(lst)