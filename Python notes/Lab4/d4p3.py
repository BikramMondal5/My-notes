# Read a file chess_results.csv and print each lines of the file.

# b)Reading Files
with open("chess_results.csv","r") as file:
   content = file.read()
   print(content)
   