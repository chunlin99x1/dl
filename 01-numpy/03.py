import numpy as np
# 统计函数
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(np.mean(arr,axis=0)) # axis 0 表示横向
print(np.mean(arr,axis=1)) # 竖向
print(np.sum(arr,axis=0))
print(np.sum(arr)) # 不考虑维度  全部元素相加
# max min
print(np.max(arr,axis=0))
print(np.min(arr))
# 标准差
print(np.std(arr,axis=0))
# 方差
print(np.var(arr,axis=0))
# 最大索引
print(np.argmax(arr,axis=0))
# cumsum 返回一个累加数组
print(np.cumsum(arr,axis=0))
# cumprod 返回一个累乘数组
print(np.cumprod(arr,axis=0))

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.any(arr1>5,axis=1))
# all
print(np.all(arr1>5,axis=0))








