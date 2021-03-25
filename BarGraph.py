import matplotlib.pyplot as plt

plt.style.use('ggplot')

x = [1, 2, 3]
y = [2, 4, 3]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, y)
# plt.xlabel("")
plt.ylabel("Height")
# plt.title("xxx")

plt.xticks(x_pos, x)

plt.show()
