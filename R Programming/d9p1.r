#install.packages('caTools')
#install.packages('party')
#install.packages('dplyr')
#install.packages('magrittr')
#install.packages('rpart')
#install.packages('rpart.plot')

library(caTools)
library(party)
library(dplyr)
library(magrittr)
library(rpart)
library(rpart.plot)

data = iris
data
nrow(data)
sample_data = sample.split(data, SplitRatio = 0.75)
train_data = subset(data, sample_data==TRUE)
train_data
nrow(train_data)
test_data = subset(data,sample_data==FALSE)
test_data
nrow(test_data)

model = rpart(Species ~ .,data=train_data, method ="class")
rpart.plot(model)


predict_model = predict(model, newdata=test_data, type="class")
n_at = table(predict_model, test_data$Species)
n_at

ac=sum(diag(n_at))/sum(n_at)
ac
