# Write a code with exception handling to open a file. Test the code with a wrong path and execute the exception.

try:
    with open("MyName.txt","r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file wasn't found")