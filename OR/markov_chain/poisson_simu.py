import numpy as np
from matplotlib import pyplot as plt 

lam = np.array([0.5, 1])  # 参数为1.5的泊松过程
T = 10  # 时间到T
n = np.random.poisson(lam * T, (10,2))  # T时间内发生的次数
print(n)

# 生成 n 个[0, T]均匀分布随机数并排序
t = np.hstack([[0], np.sort(np.random.random(n) * T)])

for i in range(n):
    plt.plot((t[i], t[i+1]), (i, i), c='r')

plt.plot((t[i+1], T), (n, n), c='r')
plt.xlim([0, T])
plt.ylim([0, n+0.5])
plt.show()



import numpy as np
s = np.random.poisson(5, 10000)

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 14, density=True)
plt.show()

