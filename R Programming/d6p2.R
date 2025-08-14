# Create a random vector and find the nth highest value of that vector where n is the given by the user
random = sample(1:20,5)
sorted_random = sort(random, decreasing=TRUE)
print(sorted_random)

print(sorted_random[num])


num = as.integer(readline("Enter the number: "))