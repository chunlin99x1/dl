import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold  # 地方差过滤法

### 低方差过滤法
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

###  皮尔逊相关系数
from  pathlib import Path
base_path = Path(__file__).parent
# 使用数据集
adv = pd.read_csv(base_path / "data" / "advertising.csv")
print(adv.head())
print(adv.index)
print(adv.columns)
#丢弃掉id
adv.drop(columns=["Unnamed: 0"],inplace=True)
# adv.drop(columns=adv.columns[0],inplace=True)
print(adv.head())
adv.dropna(inplace=True) # 删除空值
print(adv.shape)
# 提前特征 和 目标值
# x  = adv[["TV", "Radio", "Newspaper"]]
x = adv.drop(columns=["Sales"], inplace=False)
print(x.head())
y = adv["Sales"]
print(y.head())
# 计算皮尔逊相关系数
corr_matrix = x.corrwith(y)
print(corr_matrix)
# 画图
import matplotlib.pyplot as plt
corr_matrix.plot.bar()
#plt.show()

#相关性系数矩阵
corr_matrix = x.corr()

print(corr_matrix)
import seaborn as sns
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
# plt.show()




## SelectKBest
from sklearn.feature_selection import SelectKBest,f_classif  # 保留得分最高的k个特征
data = pd.read_csv(Path(__file__).parent / "data" / "heart_disease.csv")
print(data.head())
features = data.drop(columns=["是否患有心脏病"])
target = data["是否患有心脏病"]
selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(features, target)
# 获取选择的特征
selected_features = selector.get_support()
print(selected_features)  # False False  True False False False False  True  True  True False  True False]
print("选择到特征有",features.columns[selected_features].tolist()) # ['胸痛类型', '最大心率', '运动性心绞痛', '运动后的ST下降', '主血管数量']
# 获取到 特征的得分
scores = selector.scores_.round(2)
print(dict(zip(features.columns, scores)))

print(scores)



















