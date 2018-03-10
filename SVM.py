from sklearn import svm

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create svm classification object

model = svm.SVC()

# train model using the training sets and check result

model.fit(x_train, y_train)
model.score(x_train, y_train)

# predict output

predicted = model.predict(x_test)