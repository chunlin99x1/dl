import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 默认字体不含中文，标题/坐标轴上的中文会显示成方框
plt.rcParams["font.sans-serif"] = ["PingFang SC", "Heiti SC", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False  # 修复负数坐标轴的负号显示

# 判断两个series 是否相同
s1 = pd.Series([1,3,5,7,9],index=['a','b','c','d','e'])
s2 = pd.Series([1,3,5,7,9],index=['a','b','c','d','e'])
print(s1.equals(s2))  #  true
print(s1 == s2) # 返回的使用 全true的 series
print(s1.keys()) # Index(['a', 'b', 'c', 'd', 'e'], dtype='str')

arr3 = pd.Series([3,2,1])
arr4 = pd.Series([6,7,8])
#corr 相关系数  完全正相关的，相关系数为 1  完全不相关是 0
print(arr3.corr(arr4))
arr5 = pd.Series([1, -1, 1, -1])
arr6 = pd.Series([1, 1, -1, -1])
print(arr6.corr(arr4))
print(arr5.corr(arr6))

print("---------------")
# cov（） 计算与另一个series的协方差
# 协方差用于衡量两个变量的总体误差  其值的正负表示两个变量的变化方向 正值表示同向变化，负值表示反向变化。
print(arr4.cov(arr3))

# hist 直方图：把数据按 bins 指定的区间个数分组，统计每组内的数量
# 注意：arr4 只有 3 个数、bins=3 时每个区间恰好只有 1 个数，
# 柱子会顶满整个坐标区，看起来像一块纯色方块（并不是没画出来）
ax = arr4.hist(bins=3, edgecolor="white", lw=1)
print(type(ax))  # 返回的是 matplotlib.axes.Axes 对象
print(ax.patches[0].get_x(), ax.patches[0].get_height())  # 第一根柱子的左边界、高度

# 换成更多数据、更多区间，才能看到真正的分布形状
data = pd.Series(np.random.normal(loc=10, scale=3, size=200))
ax2 = data.hist(bins=20, edgecolor="white")  # 得到的对象是 matplotlib.axes.Axes 对象
ax2.set_xlabel("取值")
ax2.set_ylabel("频数")
ax2.set_title("200 个正态分布随机数的直方图")

# 显示图（只弹一次窗口，展示全部 figure）
plt.tight_layout()
plt.show()


















