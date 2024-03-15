import numpy as np
import math
# X_train(n, m); y_train(n,)
class LinearRegression():
    def __init__(self) -> None:
        self.A = None
        self.b = None
        self.learing_rate = 1e-3
        self.threshold = 1e-3
        self.epoch = 1000
    def fit(self, X_train, y_train):
        # initialize parameter
        self.A = np.random.uniform(size=X_train.shape).T
        self.b = np.random.uniform(size=y_train.shape)
        gradient = np.inf
        epoch = 0
        while abs(gradient) > self.threshold and epoch < self.epoch:
            # compute y
            print(epoch, gradient)
            y = self.A @ X_train + self.b
            
            # compute loss
            loss = sum((y - y_train)**2) / y.shape[0]
            # loss = math.sqrt(loss)
            
            # compute gradient: dao ham cua loss voi input
            # loss = (ax+b - y_train)**2
            # loss' = 2ax 
            gradient = 2 * self.A @ X_train
            
            # update A, b
            self.A -= gradient * self.learing_rate
            self.b -= gradient * self.learing_rate
            
            epoch += 1
        print(gradient)
    def predict(self, X_test):
        return self.A @ X_test + self.b #nhan ma tran
    
X = np.random.uniform(size=(1000, 2))
y = np.random.uniform(size=(1000, 1))
X_train = X[:800, np.newaxis, 0]
X_test = X[800:, np.newaxis, 0]
y_train = y[:800, :]
y_test = y[800:, :] 

model = LinearRegression()
model.fit(X_train, y_train)
model.predict()
