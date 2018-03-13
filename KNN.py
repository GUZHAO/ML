# before doing KNN make sure that
# 1.normalize the features to avoid high value outlier
# 2.data cleaning

from sklearn.neighbors import KNeighborsClassifier

# load train and test sets

x_train = input_variables_values_training_datasets

y_train = target_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create KNeighbors classifier object

model = KNeighborsClassifier(n_neighbors=6)

# default value of n_neighbors is 5

# train model using the training sets and check result

model.fit(x_train, y_train)

# predict output

predict = model.predict(x_test)
