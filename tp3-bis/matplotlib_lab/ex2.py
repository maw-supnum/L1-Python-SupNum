# 1 -
import numpy as np


def G(x):
    x = float(x)
    if not (0 <= x and x < 2): # not (0 <= x < 2)
        raise ValueError("x devrait etre dans [0, 2[")
    # 0 <= x < 1
    elif 0 <= x and x < 1:
        return x
    else:
        return 1

# 2-
# pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt

# print([G(x) for x in (np.arange(0, 200) / 100)])
X = np.arange(0, 200) / 100
# y = [G(x) for x in X]
# classic
y = []
for elm in X:
    y.append(G(elm))
y = np.array(y)


plt.figure("G: x -> G(x)")
plt.plot(X, y)
plt.show()





