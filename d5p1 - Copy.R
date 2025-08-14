# Find the mean
x=c(1,2,3,4,5,6,7,8,9)
mean(x)
mean(x,trim=0.3)

# Find the median
median(x)
y=c(1,2,3,4,5,6,7,8)
median(y)

# Find the mode
z=c(12,34,56,4,56,56,4,67)
table(z)
which.max(table(z))

v=c(12,34,56,4,56,56,4,6)
v1 = unique(v)
v1[which.max(tabulate(match(v,v1)))]
