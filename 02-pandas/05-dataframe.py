import pandas as pd
# 创建 df
data = {
    'name': ['张三', '李四', '王五'],
    'age': [18, 19, 20],
    'sex': ['男', '女', '男']
}


df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df.index)
print(df.values)




