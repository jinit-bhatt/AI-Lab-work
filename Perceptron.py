import numpy as np
class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
        for epoch in range(self.epochs):
            for i in range(len(X)):
                y_pred = self.predict(X[i])
                if y_pred != y[i]:
                    self.weights += self.learning_rate * (y[i] - y_pred) * X[i]
                    self.bias += self.learning_rate * (y[i] - y_pred)

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        y_pred = np.where(y_pred >= 0, 1, 0)

        return y_pred

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([1, 0, 1])
perceptron = Perceptron()
perceptron.fit(X, y)
X_new = np.array([[7, 8], [9, 10]])
y_pred = perceptron.predict(X_new)
print(y_pred)
