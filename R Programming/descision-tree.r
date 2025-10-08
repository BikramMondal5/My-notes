# =============================
# Decision Tree in R (Classification)
# =============================

# Step 1: Install & load required libraries
install.packages("rpart")
install.packages("rpart.plot")

library(rpart)
library(rpart.plot)

# Step 2: Load dataset
data(iris)
head(iris)

# Step 3: Split dataset into training and testing sets
set.seed(123)  # for reproducibility
train_index <- sample(1:nrow(iris), 0.7 * nrow(iris))
train_data <- iris[train_index, ]
test_data <- iris[-train_index, ]

# Step 4: Build the Decision Tree model
model <- rpart(Species ~ ., data = train_data, method = "class")

# Step 5: Display the model summary
print(model)
summary(model)

# Step 6: Visualize the Decision Tree
rpart.plot(model, main = "Decision Tree for Iris Dataset", type = 2, extra = 104)

# Step 7: Make predictions on the test data
predictions <- predict(model, test_data, type = "class")

# Step 8: Evaluate the model
confusion_matrix <- table(Predicted = predictions, Actual = test_data$Species)
print(confusion_matrix)

# Calculate accuracy
accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
cat("Model Accuracy:", round(accuracy * 100, 2), "%\n")

# Step 9: Check the complexity parameter table
printcp(model)
plotcp(model, main = "Complexity Parameter Plot")

# Step 10: Prune the tree (to avoid overfitting)
# Select the cp value that gives lowest cross-validation error
best_cp <- model$cptable[which.min(model$cptable[,"xerror"]), "CP"]
pruned_model <- prune(model, cp = best_cp)

# Step 11: Visualize pruned tree
rpart.plot(pruned_model, main = "Pruned Decision Tree", type = 2, extra = 104)

# Step 12: Predict again using pruned model
pruned_pred <- predict(pruned_model, test_data, type = "class")
pruned_conf <- table(Predicted = pruned_pred, Actual = test_data$Species)
print(pruned_conf)

# Step 13: Pruned model accuracy
pruned_acc <- sum(diag(pruned_conf)) / sum(pruned_conf)
cat("Pruned Model Accuracy:", round(pruned_acc * 100, 2), "%\n")
