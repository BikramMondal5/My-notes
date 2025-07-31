letters_lower = letters       
letters_upper = LETTERS         

first_10_lower = letters_lower[1:10]

last_10_upper = letters_upper[17:26]

special_upper = toupper(letters_lower[22:24])

print("First 10 letters (lowercase):", paste(first_10_lower, collapse = " "), "\n")
print("Last 10 letters (uppercase):", paste(last_10_upper, collapse = " "), "\n")
print("22nd to 24th letters (uppercase):", paste(special_upper, collapse = " "), "\n")
