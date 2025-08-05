# 1. Write the following piece of commands in your lab file

# a)Opening Files
file = open("example.txt","w")

# b)Reading Files
file = open("example.txt","r")
content = file.read()
print(content)

# c)Writing Files
file = open("example.txt","w")
file.write("I'm a B.TECH student from HITK")

# d)Closing Files
file.close()

# e)Context Manager
with open("example.txt","r") as file:
    content = file.read()
    print(content)