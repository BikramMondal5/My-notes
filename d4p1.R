d1 = data.frame(sl.no=c(1,2), Name=c("John","Dora"),  Age=c(21,15))
print(d1)
index = which(d1$Name=="John")
d1$Age[index] = 25
print(d1)


# Add new column
d1$State = c("Kolkata","Mumbai")
print(d1)

# Delete a column
d1$Age=NULL
print(d1)
