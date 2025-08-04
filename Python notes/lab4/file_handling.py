# 1. Answer the following questions using python

# a)Opening Files
file = open("example.txt", "w")

# b)Reading Files
file = open("example.txt", "r")
content = file.read()
print(content)

# c)Writing Files
file = open("example.txt", "w")
file.write("My name is Alice")

# d)Closing Files
file.close()

# e)Context Manager
with open("ecample.txt", "r") as file:
    content = file.read()
    print(content)

