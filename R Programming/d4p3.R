d1 = data.frame(Name=c("abc","xyz","pqr"), Age=c(30,31,11),  Height=c(168,179,139), Weight=c(57,69,32), Gender=c("F","M","M"))
print(d1)
print("Name. of employers")
print(d1$Name)

# Convert gender into factor
factor = as.factor(d1$Gender) 
print(factor)
is.factor(factor)

# Arrange accroding to the order
print(d1)
newDF = d1[order(d1$height)]
print(newDF)