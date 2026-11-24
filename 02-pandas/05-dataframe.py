import pandas as pd
# 创建 df
data = {
    'name': ['张三', '李四', '王五', '王五'],
    'age': [18, 19, 19, 20],
    'sex': ['男', '女', '男', '男']
}


df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.index)
print(df.values)
# 维度
print(df.ndim)
# 形状
print(df.shape)

# 元素个数
print(df.size)
# 转置
print(df.T)
#显示索引
print(df.loc[0])
print(df.isna())

print(df["age"].sum())
print(df["age"].mean())
print(df["age"].max())
print(df["age"].min())
print(df["age"].var())
print(df["age"].std())
# 中位数
print(df["age"].median())
# 分位数
print(df["age"].quantile(q=0.5))
print(df.describe()) # 场景的统计信息
print(df.info())
"""
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    3 non-null      str  
 1   age     3 non-null      int64
 2   sex     3 non-null      str  
dtypes: int64(1), str(2)
memory usage: 204.0 bytes
None
"""

print(df.count())  # 非空元素的个数
"""
name    3
age     3
sex     3
dtype: int64
"""
# 去重
print(df.duplicated()) # 检查重复行
"""
0    False
1    False
2    False
3     True
dtype: bool
"""
print(df.drop_duplicates()) # 丢弃重复行
# 指定 subset
print(df.drop_duplicates(subset=[ 'age']))
# 采样
print(df.sample(frac=0.5)) # 表示随机采样50%的行
print(df.replace(["王五",18], ["王六",28]))
# 判断两个df是否相等

df1 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
df2 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
print(df1.equals(df2))

df3 = pd.DataFrame({'A': [2, 5, 3, 7, 4],'B': [1, 6, 2, 8, 3]})
print(df3.cumsum()) # 累计最大值
print("====================")
# diff 计算相邻元素的差
print(df3.diff())
# sort_index
print(df3.sort_index())

# 删除列
print(df3.drop(columns=['A'],axis=0))
# 插入一列
df3.insert(1, 'C', [6,6,6,6,6])
print(df3)
import  os
os.makedirs("data", exist_ok=True)
df3.to_csv("data/data.csv", index=False) #  to_csv
df3.to_excel("data/data.xlsx", index=False)
# to_pickle
df3.to_pickle("data/data.pkl", protocol=4) # protocol=4 表示使用 protocol 4 序列化 默认是 3

df3.to_clipboard(index=False) # to_clipboard 复制到剪贴板
x = df3.to_dict("records")
print(x)
df3.to_json("data/data.json", orient="values")



















