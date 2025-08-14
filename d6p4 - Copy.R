x1 = c(1,2,3,4,999,1,"NA",1,1,"NA")
x2 = c(1,2,3,4,5,1,"NA",1,1,"NA")
x3 = c("a","b","c","xx","x",44,"x","a","a","NA")
x4 = c("","","","","","","","","","")
x5 = c("NA","NA","NA","NA","NA","NA","NA","NA","NA","NA")

data = data.frame(x1,x2,x3,x4,x5)
print(data)

sum(is.na(data))

data$x1[data$x1=="NA"] = NA
data$x2[data$x2=="NA"] = NA
data$x3[data$x3=="NA"] = NA
data$x4[data$x4==""] = NA
data$x5[data$x5=="NA"] = NA
print(data)

data = data[rowSums((is.na(data))!=ncol(data)),]

print(data)

na.omit(data)