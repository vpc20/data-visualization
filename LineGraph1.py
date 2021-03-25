import matplotlib.pyplot as plt
import numpy as np

# x = [0, 1, 2, 3, 4, 5, 6, 7]
# y = [73, 74, 75, 71, 69, 72, 76, 73]
# plt.title('Daily Temperatures')
# plt.xlabel('day')
# plt.ylabel('temp')

x = [0, 1, 2, 3, 4, 5]
y = [7, 1, 5, 3, 6, 4]
plt.title('Stock Prices')
plt.xlabel('day')
plt.ylabel('price')

plt.grid()
plt.plot(x, y, '-o')
# plt.yticks(np.arange(0, -5, -1))

plt.show()
