import numpy as np
import pandas as pd

# 定义series
s = pd.Series([1,3,5,7,9,None,np.nan,5],index=['a','b','c','d','e','f','g','h'],name='series')
print(s.head()) # 默认显示前5个
print(s.tail()) # 默认显示后5个
# isin 判断是否在某个集合中
print(s.isin([11,2,3]))
#判断series 中是否有缺失值
print(s.isnull()) # 后面两个是true

# 求和
print(s.sum())
# 平均值
print(s.mean())
# 最大 最小
print(s.max(),s.min())
# 方差
print(s.var())
#标准差
print(s.std())
# 中位数
print(s.median()) # 如果元素个数为偶数 中位数就是排序后位于中间的两个元素的平均值
# 众数 mode
print(s.mode())
# 分位数
print(s.quantile(0.1, interpolation="midpoint")) # 解释一下 interpolation="midpoint" 表示如果分位数不在元素中，则取中间两个元素的平均值
# 解释一下 quantile 0.1 表示取10%的分位数  作用是取10%位置的值

# 0.25 分位数就是将数据从小到大排序后，位于 25% 位置处的数值。  分位数的作用 是将数据进行分段，比如将数据分成四段，第一段占25%，第二段占25%，第三段占25%，第四段占25%。

#常见的统计信息
print(s.describe()) # 常见的统计信息
# values_counts 每个元素的个数
print(s.value_counts())

# 非缺失元素的个数
print(s.count())
# 去重
print(s.drop_duplicates())# 元素去重  返回新的series
print("=============")
# unique
print(s.unique()) # [ 1.  3.  5.  7.  9. nan] # 返回是一个数组

### 随机采样
print(s.sample(3))
# replace  指定值代替原有值
print(s.replace(5,10))
# toframe 转化成DataFrame对象
print(s.to_frame())

















































