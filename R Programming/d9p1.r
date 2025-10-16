library(caTools)
library(party)
library(dplyr)
library(magrittr)
library(rpart)
library(rpart.plot)

age = c("youth","youth","mid_aged","senior","senior","senior","mid_aged","youth","youth","senior","youth","mid_aged","mid_aged","senior")
income = c("high","high","high","medium","low","low","low","medium","low","medium","medium","medium","high","medium")
student = c("no","no","no","no","yes","yes","yes","no","yes","yes","yes","no","yes","no")
credit_rating = c("fair","excellent","fair","fair","fair","excellent","excellent","fair","fair","fair","excellent","excellent","fair","excellent")
buys_comp = c("no","no","yes","no","no","yes","yes","no","yes","no","yes","yes","yes","yes")

data = data.frame(age,income,student,credit_rating,buys_comp)
nrow(data)
data

table(data$buys_comp)[1]
p1=table(data$buys_comp)[1]/nrow(data)
p2=table(data$buys_comp)[2]/nrow(data)

entropy_entire_data = (-1*p1*log2(p1))-(p2*log2(p2))
entropy_entire_data

# Entropy of the age

ageData = table(data$age,data$buys_comp)
ageData

# 1. Entropy of the youth
p1=ageData[3,2]/(ageData[3,2]+ageData[3,1])
p2=ageData[3,1]/(ageData[3,2]+ageData[3,1])
entropy_youth = (-1*p1*log2(p1))-(p2*log2(p2))
entropy_youth

# 2. Entropy of the mid-aged

ageData

p1=ageData[2,2]/(ageData[2,1]+ageData[2,2])
p2=ageData[2,1]/(ageData[2,1]+ageData[2,2])
entropy_mid_aged = (-1*p1*log2(p1))-(p2*log2(p2))
entropy_mid_aged

# 3. Entropy of the senior

ageData

p1=ageData[1,2]/(ageData[1,2]+ageData[1,1])
p2=ageData[1,1]/(ageData[1,2]+ageData[1,1])
entropy_senior = (-1*p1*log2(p1))-(p2*log2(p2))
entropy_senior

if (is.nan(entropy_senior)) {
  entropy_senior = 0
}


info_gain = entropy_entire_data - ((5/14)*entropy_youth - (4/14)*entropy_mid_aged - (5/14)*entropy_senior)
info_gain
