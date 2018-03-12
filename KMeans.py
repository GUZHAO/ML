from sklearn.cluster import KMeans

# load train and test sets

x_train = input_variables_values_training_datasets

x_test = input_variables_values_test_datasets

# create Kneighbors classifier object

model = KMeans(n_clusters=3, random_state=0)

# train the model using the training sets and check result

model.fit(x_train)

# predict output

predicted = model.predict(x_test)
