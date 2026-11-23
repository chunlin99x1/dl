# matrix 是 ndarray的子类 只能生成二维矩阵
import numpy as np
from sympy import print_glsl

arr = np.matrix("1 2 ; 3 4")
print(arr)
arr  = np.matrix([[1,2],[3,4]])
print(arr)

arr1 = np.array([1,2,3],dtype=np.int32)
print(arr1,type(arr1))
# 也可以使用 astype
arr1 = arr1.astype(np.int64)
print(arr1,type(arr1),arr1.dtype,arr1.nbytes,arr1.itemsize)
## ndarray切片和索引
arr = np.arange(10)
print(arr)
print(arr[0:2])
print(arr[slice(0,9,2)])
print(arr[0:9:2])

### 常用函数
arr = np.random.randn(3,3)
print(arr)
print("-------- 原arr -----------")
print(np.abs(arr)) # 各元素绝对值
# ceil
print(np.ceil(arr)) # 向上
print(np.floor(arr)) # 向下
# 四舍五入
print(np.rint(arr))
print(np.round(arr))

#  判断元素是否是NaN
print(np.isnan(arr))

# 两个形状相同的arr 元素相乘
print(np.multiply(arr,arr))
# 相加
print(np.add(arr,arr))
# 相除
print(np.divide(arr,arr))
# 三元表达式
print(np.where(arr>0,1,0))





















