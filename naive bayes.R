library(e1071)

#load train and test sets

X_train <- input_variables_values_training_datasets
y_train <- target_variables_values_training_datasets
x_test <- input_variables_values_test_datasets

x <- cbind(x_train, y_train)

#fit model

m <- naiveBayes(y_train ~ . , data = x)
summary(m)

#predict output

predicted <- predict(m, x_test)