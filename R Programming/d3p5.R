

d1 = data.frame(X1=c(1:5), X2=head(letters,5),  X3=3)
print(d1[which(d1$X1>=3),])
