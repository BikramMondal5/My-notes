temp = c(22, 27, 26, 24, 23, 26, 28)
barplot(temp, main="Height of 7 cities", xlab="Cities", ylab="Max. Temp", names.arg = c("Kol","Del", "Mum","Beng","Chen","Bhub","Luck"), col="red", border="blue",density=30)

age = c(17,18,18,17,18,19,18,16,18)
barplot(table(age))
hist(age)

