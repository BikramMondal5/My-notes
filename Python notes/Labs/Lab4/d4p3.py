# Read a file chess_results.csv and print each lines of the file.

with open("chess_results.csv","r") as file:
   content = file.readlines()
   for line in content:
    print(line.strip())