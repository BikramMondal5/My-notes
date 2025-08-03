# create 3 vector A, B, C with 3 integer. Combine these three vectors to create 3x3 matrix where each column represents a vector and print the content of the matrix
A = c(3L, 5L, 7L)
B = c(9L,12L,15L)
C = c(18L, 21L, 24L)

arr = array(c(A,B,C),dim=c(3,3))
matrix = as.matrix(arr)

print(matrix)
