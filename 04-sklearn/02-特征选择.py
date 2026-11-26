import numpy as np
from sklearn.feature_selection import VarianceThreshold  # 地方差过滤法
a = np.random.randn(10000) # 均值是0，方差是1
print("a的方差是：", a.var(), "a的均值是：", a.mean())
# 构造特征  均值是5标准差 0.1
b = np.random.normal(size=10000, loc=5, scale=0.1)
print("b的方差是：", b.var(), "b的均值是：", b.mean())
X = np.vstack([a, b]).T # vstack 垂直堆叠  水平堆叠用hstack
print(X)
# 过滤掉 方差是0.2的特征
var_thresh = VarianceThreshold(threshold=0.2)
X_filtered = var_thresh.fit_transform(X)
print(X_filtered)  # 只保留了 






