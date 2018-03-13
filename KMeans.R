library(cluster)

#load train and test sets

X_train <- input_variables_values_training_datasets
x_test <- input_variables_values_test_datasets

#fit model

m <- kmeans(data = x_train, 3)
summary(m)

#predict ouput

predicted <- predict(m, x_text)