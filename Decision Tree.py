from sklearn import tree

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create tree object

model = tree.DecisionTreeClassifier(criterion='gini')  # by default

model2 = tree.DecisionTreeRegressor()

# train model using the training sets and check result

model.fit(x_train, y_train)
model.score(x_train, y_train)

# predict output

predicted = model.predict(x_test)

# need to master all methods for example not only gini but also
# 1.information gain
# 2.chi-square
# 3.entropy
