a = 10

def call():
    global a
    a = 15
    b = 20
    print(a)

call()

# Output: 15