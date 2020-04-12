import numpy as np

points = [[0.05, 0.54], [0.10, 0.51], [0.17, 0.47],
          [0.25, 0.45], [0.30, 0.42], [0.36, 0.38]]


# Creating coefficients

def createCoefficients(points, m):
    n = len(points)
    c = [[0 for i in range(m + 1)] for j in range(m + 1)]
    fm = [0 for i in range(m + 1)]
    for k in range(m + 1):
        for j in range(m + 1):
            for i in range(n):
                c[k][j] += points[i][0] ** (j + k)
        for i in range(n):
            fm[k] += points[i][1] * points[i][0] ** k
    coef = np.ndarray.tolist(np.linalg.solve(np.array(c), np.array(fm)))
    return coef


# Creating polynoms

def createPolynom(points, m):
    coefficients = createCoefficients(points, m)
    polynom = "y = "
    for i in range(len(coefficients)):
        polynom += "{:.3f} * x^{} + ".format(coefficients[i], i)
    polynom = polynom[:len(polynom) - 2]
    print(polynom)

# Executing

createPolynom(points, 1)
createPolynom(points, 2)
createPolynom(points, 3)
