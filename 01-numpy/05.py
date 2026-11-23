import numpy as np
# 矩阵乘法
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[6, 5, 4], [3, 2, 1]])

print(arr1 * arr2) # 对应位置相乘
print(np.multiply(arr1, arr2))  # 对应位置相乘


arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # 2行3列
arr2 = np.array([[6, 5], [4, 3], [2, 1]]) # 3行2列
# 点乘   np.dot    @   arr.dot
print(np.dot(arr1, arr2))
print(arr1 @ arr2)
print(arr1.dot(arr2))

