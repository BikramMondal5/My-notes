x1 = c("i","I",1,"a")
x2 = c("NA","NA","NA","NA")
x3 = c("iii","III",3,6)
x4 = c("iv","IV",4,"d")
x5 = c("NA","NA","NA","NA")
x6 = c("vi","VI",6,"F")
x7 = c("NA","NA","NA","NA")
x8 = c("viii","VIII",8,"h")
x9 = c("NA","NA","NA","NA")
x10 = c("x","X",10,"j")
data = data.frame(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
print(data)

data$x2[data$x2=="NA"] = NA
data$x5[data$x5=="NA"] = NA
data$x7[data$x7=="NA"] = NA
data$x9[data$x9=="NA"] = NA
print(data)

row3 = data[3, ]
new_data=is.na(data)
sum = 0
count = 0
for (element in row3) {
  if(is.na(element) == FALSE){
    int_element = as.integer(element)
    sum = sum + int_element
    count = count+1
  }
 
}
mean1 = sum/count
print(mean1)

row_three = data[3,]
for (element in row_three) {
  if(is.na(element) == TRUE){
   element == mean1
  }
  
}

print(row_three)