# Create a function to read a list of numbers = [4, 7, 2, 9, 1, 5, 3]. Take a target value(say 9) from list and then iterate a loop to check the value. Once you get the target value break the condition. Print the  numbers in the list before you find the target.

def checkNum(*args):
    target = 9
    #print(args)
    for num in args: 
        print(num)
        if num == target:
            print(f"Found {target}!") 
            break  # Exit loop once target is found
        print("Search complete")

checkNum(4, 7, 2, 9, 1, 5, 3)