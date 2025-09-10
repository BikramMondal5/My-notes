import functools
def cumul_sub(x, y):
    return (x - y)

lst = [6, 5, 4, 3, 2, 1]
print(functools.reduce(cumul_sub, lst))

# Output: -9

# Explanation: 

# 1. Start with the first two elements:
# 6-5 =1
# 2. Take result and next element:
# 1-4 = -3
# 3. Next:
# -3-3 =- 6
# 4. Next:
# -6-2 = -8
# 5. Next:
# -8-1 = -9


