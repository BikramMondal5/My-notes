with open("HelloWorld.txt", "r") as file:    
    # Read all content at once    
    content = file.read()    
    print(content)

with open("HelloWorld.txt", "r") as file:    
 for line in file:        
    print(line.strip())