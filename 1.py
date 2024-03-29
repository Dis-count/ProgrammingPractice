#  通过修改一串数中的一个数字使得
#  这一串数字 是 非递减数列  满足就输出 true 不满足就输出 false
#  例如 3 4 1 2  不可以通过 修改 4 -> 3 而得到 非递减数列
# 因而可以判断  至多只有一个波段 才可以满足修改一个数字得到非递减数列
from matplotlib import pyplot as plt


# num[i] \geq num[i+1] and num[i-1] \geq num[i+1]
# 超过一个起伏  即可判断 不满足