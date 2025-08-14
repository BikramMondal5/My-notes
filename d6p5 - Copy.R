dataset = iris
print(dataset)
boxplot(dataset)

out = boxplot.stats(dataset$Sepal.Width)$out
out
out_index = which(dataset$Sepal.Width %in% c(out)) 
print(out_index)

dataset$Sepal.Width[out_index] = NA
print(dataset$Sepal.Width)