import functools
def cumul_sub(x, y):
    return (x - y)

lst = [6, 5, 4, 3, 2, 1]
print(functools.reduce(cumul_sub, lst))

# Output: -19