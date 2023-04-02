# import matplotlib.pyplot as plt

x = []
y = []
for n in range(30):
    for i in range(n + 1):
        # y.append(pow(16, n - i, 8 * i + 1))
        # x.append(i)
        print(str(pow(16, n - i, 8 * i + 1)).ljust(4), end="|")
    print()

# plt.bar(x, y)
# plt.show()
