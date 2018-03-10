library(rpart)

#load train and test sets

X_train <- input_variables_values_training_datasets
y_train <- target_variables_values_training_datasets
x_test <- input_variables_values_test_datasets

x <- cbind(x_train, y_train)

#grow tree

m <- rpart(y_train ~ ., data = x, method = "class")
summary(m)

#predict output

predicted <- predict(m, x_test)