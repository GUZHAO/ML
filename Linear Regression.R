#load train and test sets

X_train <- input_variables_values_training_datasets
y_train <- target_variables_values_training_datasets
x_test <- input_variables_values_test_datasets

x <- cbind(x_train, y_train)

#train the model using the traing sets and check result

m <- lm(y_train ~ ., data = x)
summary(m)

#predict

predicted <- predict(m, x_test)