#load train and test sets

X_train <- input_variables_values_training_datasets
y_train <- target_variables_values_training_datasets
x_test <- input_variables_values_test_datasets

x <- cbind(x_train, y_train)

#train the model using the training sets and check score

m <- glm(y_train ~., data = x, family = 'binomial')
summary(m)

#predict output

predicted <- predict(m, x_test)