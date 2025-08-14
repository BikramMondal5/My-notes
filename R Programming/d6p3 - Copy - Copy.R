x1 = c(3,13,13)
x2 = c(13,17,13)
x3 = c(1,5,14)
x4 = c(11,14,11)

data = data.frame(x1,x2,x3,x4)
print(data)

print(rowSums(data))
print(colSums(data))

colsum = colSums(data)
rowsum = rowsum(data)
dataframe = rbind(data,colsum)
data$colsum
print(data)