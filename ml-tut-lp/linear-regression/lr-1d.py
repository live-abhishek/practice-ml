import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

for line in open("data1.csv"):
    x,y = line.split(",")
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

# as per my derived formula
denominator = X.dot(X).mean() - X.mean() * X.mean()
a = ( X.dot(Y).mean() - X.mean() * ( Y.mean() ) ) / denominator
b = ( Y.mean() * ( X.dot(X).mean() ) - X.mean()*( X.dot(Y).mean() ) ) / denominator

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

print(a, b)

# calculated predicted Y
Yhat = a*X + b

# plot it all
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("the r-squared is:", r2)
