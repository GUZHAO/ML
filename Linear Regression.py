from sklearn import linear_model

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create linear regression object

model = linear_model.LinearRegression()

# train the model using the training sets and check score

model.fit(x_train, y_train)
model.score(x_train, y_train)

# check coefficient and intercept

print('coefficient: n', model.coef_)
print('Intercept: n', model.intercept_)

# predict output

predicted = model.predict(x_test)