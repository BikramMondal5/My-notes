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
sample_data = sample.split(data, SplitRatio = 0.85)
train_data = subset(data, sample_data==TRUE)
train_data
nrow(train_data)
test_data = subset(data,sample_data==FALSE)
test_data

model = rpart(buys_comp ~ .,data=train_data, method ="class")
rpart.plot(model)


predict_model = predict(model, newdata=test_data, type="class")
n_at = table(predict_model, test_data$buys_comp)
n_at

ac=sum(diag(n_at))/sum(n_at)
ac
