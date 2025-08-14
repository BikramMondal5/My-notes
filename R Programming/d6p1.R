# Define the dataset
col1 = c(1:10)
col2 = c(11:20)
col3 = c(21:30)
col4 = c(1:10)

dataset = data.frame(col1, col2, col3, col4)

cor(col1,col2)
cor(col1,col3)
cor(col1,col4)
cor(col3,col4)

# Correlation between col1, col4, and col2
correlation1 = cor(dataset[, c("col1", "col4", "col2")])
print("Correlation between col1, col4, and col2:")
print(correlation1)

# Correlation between col2, col3, and col4
correlation2 = cor(dataset[, c("col2", "col3", "col4")])
print("Correlation between col2, col3, and col4:")
print(correlation2)
