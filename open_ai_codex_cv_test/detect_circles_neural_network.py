"""
Write a neural network to detect circles.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical

# Create data
X, y = make_circles(n_samples=1000, factor=0.5, noise=0.1)

# Reshape targets to be a 2D array with one column
y = y.reshape(-1, 1)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Plot the data
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train[:, 0], cmap='winter')
plt.show()

# One hot encode the targets
encoder = OneHotEncoder()
y_train = encoder.fit_transform(y_train).toarray()
y_test = encoder.transform(y_test).toarray()

# Create the model
model = Sequential()
model.add(Dense(4, input_shape=(2,), activation='tanh'))
model.add(Dense(4, activation='tanh'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(Adam(lr=0.05), 'categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, epochs=100, verbose=1)

# Get the loss and accuracy on the test set
eval_result = model.evaluate(X_test, y_test)

# Print test accuracy
print('\n\nTest loss:', eval_result[0], 'Test accuracy:', eval_result[1])

# Plot the decision boundary
plot_decision_boundary(model, X, y).show()