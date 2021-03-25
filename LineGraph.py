import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [0, -1, -2, -1, -2, -3, -4, -3, -2]

plt.title('Countiguous Array')
plt.xlabel('index')
plt.ylabel('count')
plt.grid()
plt.plot(x, y, '-o')
plt.yticks(np.arange(0, -5, -1))

plt.show()
