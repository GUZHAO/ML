# import library

# import other necessary libraries like pandas, numpy

from sklearn import linear_model

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create linear regression object

linear = linear_model.LinearRegression()

# train the model using the training sets and check score

linear.fit(x_train, y_train)
linear.score(x_train, y_train)

# check coefficient and intercept

print('coefficient: n', linear.coef_)
print('Intercept: n', linear.intercept_)

# predict output

predicted = linear.predict(x_test)