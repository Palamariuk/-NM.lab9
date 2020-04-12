import numpy as np
import Parser
import matplotlib.pyplot as plt

points = [[0.05, 0.54], [0.10, 0.51], [0.17, 0.47],
          [0.25, 0.45], [0.30, 0.42], [0.36, 0.38]]
parser = Parser.Parser([])

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
    yield coefficients
    parser = Parser.Parser(coefficients)
    polynom = "y = " + p.get_string()
    print(polynom)
    

# Executing
cs = []
xs = []
ys = []

createPolynom(points, 1)
createPolynom(points, 2)
createPolynom(points, 3)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

for i in range(1, 4):
    cs.append(createCoefficients(points, i))
    parser = Parser.Parser(cs[i - 1])
    x, y = parser.get_tabulation_points()
    xs.append(x)
    ys.append(y)

    plt.plot(x, y, 'b')
    plt.show()

# plt.show() to show all in one page