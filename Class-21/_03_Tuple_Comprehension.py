"""
tpl_comp = (num * 10 for num in range(5+1))
print(tpl_comp) # <generator object <genexpr> at 0x0000027533AFD700>
"""

tpl_comp = *(num * 10 for num in range(5+1)),
print(tpl_comp)

tpl_comp = tuple(num * 10 for num in range(5+1))
print(tpl_comp)
