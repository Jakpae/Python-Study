import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
x = np.linspace(-7.5, 7.5, 100)
a, b, c, d = 1, 0, -25, 0
y = a*x**3 + b*x**2 + c*x + d
mu, sigma = 0.0, 50.0
noise = np.random.normal(mu, sigma, x.size) # preparation of noise
y_noise = y + noise # Y with noise
X = np.vstack([x**3, x**2, x, np.ones(len(x))]).T
poly_features = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly_features.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)
print("lin_reg model - intercept_ ({}),\n coef_({}),\nscore(X,y)= ({})".\
      format(lin_reg.intercept_, lin_reg.coef_, lin_reg.score(X_poly, y)))
x_test = X
x_poly = poly_features.transform(x_test)
y_pred = lin_reg.predict(x_poly)
plt.plot(x, y_noise, "k.", label="y_noise")
plt.xlabel("x")
plt.ylabel("y_noise, y_pred")
plt.plot(x, y_pred, "r-", label="y_pred")
plt.grid(True)
plt.title("y_noise = {:+.2f}*x**3 {:+.2f}*x**2 {:+.2f}*x {:+.2f} + noise".format(a, b, c, d))
plt.legend(loc="best")
plt.show()