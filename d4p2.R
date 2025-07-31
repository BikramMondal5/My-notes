d1 = data.frame(Name=c("Abhishek","Usha","Shreya","Vijay"), Physics=c(88,81,90,87),  Chemistry=c(82,91,85,89), Math=c(95,97,89,91))
print(d1)

# Add new column displaying marks of biology
d1$Biology = c(82,79,90,80)
print(d1)

# Aggregate marks for 1st student
index1 = which(d1$Name=="Abhishek")
marks1 = d1$Physics[index1]+d1$Chemistry[index1]+d1$Math[index1]+d1$Biology[index1]
print("Abhishek marks: ")
print(marks1)

# Aggregate marks for 2nd student
index2 = which(d1$Name=="Usha")
marks2 = d1$Physics[index2]+d1$Chemistry[index2]+d1$Math[index2]+d1$Biology[index2]
print("Usha marks: ")
print(marks2)

# Aggregate marks for 3rd student
index3 = which(d1$Name=="Shreya")
marks3 = d1$Physics[index3]+d1$Chemistry[index3]+d1$Math[index3]+d1$Biology[index3]
print("Shreya marks: ")
print(marks3)

# Aggregate marks for 4th student
index4 = which(d1$Name=="Vijay")
marks4 = d1$Physics[index4]+d1$Chemistry[index4]+d1$Math[index4]+d1$Biology[index4]
print("Vijay marks: ")
print(marks4)

# Printing the descriptive summary
print(summary(d1))