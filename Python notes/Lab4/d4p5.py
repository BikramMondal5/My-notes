# Write a code to delete a file

import os 
path = "delete.txt"
if os.path.exists(path):
   os.remove(path)
   print("The file is sucessfully deleted!")
else:
   print("The file path doesn't exist")