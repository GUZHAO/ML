from sklearn.linear_model import LogisticRegression

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create logistic regression object

model = LogisticRegression()

# train the model using the training sets and check results

model.fit(x_train, y_train)
model.score(x_train, y_train)

# check coefficient and intercept

print('coefficient: n', model.coef_)
print('intercept: n', model.intercept_)

# predict output

predicted = model.predict(x_test)

# the model can be enhanced by
# 1.adding interactions
# 2.simplifying the model characteristics
# 3.using non-linear model
# 4.using regularization to solve over-fitting

