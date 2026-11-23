# pandas是一个开源的数据分析和处理的库
import pandas as pd

# 创建一个Series 类似于一维数组  数据 + 索引
# 创建series
s = pd.Series([1,3,5,7,9],index=['a','b','c','d','e'],name='series')
print(s)
print(s.index)
print(s.name)
print(s)
print(s.index)
s1 = pd.Series([1,3,5,7,9]) # 直接指定数据
print(s1)
# 通过字段创建series
s2 = pd.Series({'a':1,'b':2,'c':3})
print(s2)

# series 的常用属性
print(s.shape) # 形状（5，）
print(s.size) # 元素个数 5
print(s.ndim)  # 维度 1
print(s.values) # 值 array([1, 3, 5, 7, 9])
print(s.index)  # 索引对象 RangeIndex(start=0, stop=5, step=1)
print(s.name) # 需要指定后才能显示 否则为None

# 切片
print(s.loc['b']) # 按照标签获取值
# 位置切片
print(s.iloc[1]) # 按照位置获取值
#复杂的切片
print(s.loc['a':'c'])


# 获取单个元素 at
print(s.at['b'])
print(s.iat[1])









