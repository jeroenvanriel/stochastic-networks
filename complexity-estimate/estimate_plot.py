import pickle
import matplotlib.pyplot as plt
from operator import truediv
import numpy as np

# load runtime measurements
(rhos, rs_0, Gs, points, runtimes_0) = pickle.load( open("runtime_result.p", "rb"))

# plot existing runtime estimates
plt.plot(rs_0, runtimes_0, 'r', label='original')

# points/second estimate
ratios = list(map(truediv, points, runtimes_0))
points_per_s = sum(ratios) / len(ratios)
print(f'points per second average = {points_per_s}')

# to see whether they somewhat converge
# (they did not really last time I checked...)
#plt.plot(ratios)
#plt.show()

# load precomputed state cardinalities
rs_1, points = pickle.load( open("points_result.p", "rb"))
rs_1 = list(rs_1)

runtimes_1 = [p / points_per_s for p in points]
plt.plot(rs_1, runtimes_1, 'b', label='state space proxy')

# try to fit a curve
x = np.asarray(rs_0 + rs_1)
y = np.asarray(runtimes_0 + runtimes_1)
x_pred = np.arange(0, 180)

# perform linear regression with quadratic features
#from sklearn.linear_model import LinearRegression
#x_quad = np.column_stack((x, x*x))
#x_quad_pred = np.column_stack((x_pred, x_pred*x_pred))

#reg = LinearRegression(fit_intercept=False).fit(x_quad, y.reshape(-1, 1))
#plt.plot(x_pred, reg.predict(x_quad_pred))

# perform non-linear curve fitting with exponential
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(b * x) + c

# uncomment to ignore the original data set for fitting
#x = np.asarray(rs_1)
#y = np.asarray(runtimes_1)

p0 = (1, 0.03, 0) # initial guess
popt, pcov = curve_fit(func, x, y, p0=p0)
plt.plot(x_pred, func(x_pred, *popt), 'y--', label='fitted curve')

plt.xlabel('r')
plt.ylabel('seconds')
plt.legend()
plt.savefig('runtime.pdf')
plt.show()

