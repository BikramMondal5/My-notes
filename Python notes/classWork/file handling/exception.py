try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")