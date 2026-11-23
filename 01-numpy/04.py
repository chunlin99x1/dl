import numpy as np
# 排序函数
arr  = np.array([[5, 0 ,5],[3, 4, 0], [2 ,6, 1]])
print(arr)
arr.sort(axis=0)
print(arr)


arr  = np.array([[5, 0 ,5],[3, 4, 0], [2 ,6, 1]])
print(arr)
arr.sort(axis=1)
print(arr)


# 去重函数
arr  = np.array([[5, 0 ,5],[3, 4, 0], [2 ,6, 1], [5, 0, 5]])
print(np.unique(arr))
print(np.unique(arr,axis=0)) #去掉重复行

# 基本运算
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** arr2) # 乘方
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4], [5], [6]]) #  会自动扩展成 [4,4,4] [5,5,5] [6,6,6]
print(arr1 + arr2)

print("===========")
arr3 = np.array([[1, 2, 3]])    [1, 2, 3] [1, 2, 3][1, 2, 3]
arr4 = np.array([[4], [5], [6]])[4, 4, 4]
print(arr3 + arr4)

