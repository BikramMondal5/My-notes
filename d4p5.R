d1 = data.frame(Sl.No=c("Survival","Non-Survival"), first=c(122,203),  second=c(167,118), third=c(528,178), crew=c(673,212))
print(d1)
d1 = as.matrix(d1)
barplot(d1,xlab="Class",col=c("red","green"))

legend("topleft", c("Survived","Not Survived"),fill=c("green","red"))