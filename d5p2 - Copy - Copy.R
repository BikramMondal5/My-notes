data = iris

# Number of row
nrow(data)

# Number of column
ncol(data)

print(data)

#Accessing a column
print(data$Petal.Width)
sapply(data,mean)
d1=data[c(-5)]
print(d1)

mode = function(d1){
  table(d1)
  v1 = unique(d1)
  result = v1[which.max(tabulate(match(d1,v1)))]
  return (result)
  
}
sapply(d1,mode)
unique(data$Species)
table(data$Species)
