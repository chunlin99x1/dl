import pandas as pd
s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
# series 和 标量的运算
print(s* 10)
# series 和 series 的运算
s1 = pd.Series([1, 1, 1, 1])
s2 = pd.Series([2, 2, 2, 2,1], index=[1, 2, 3, 4,5])
print(s1 + s2)  # 对应index位置相加 没有值就是 NaN






