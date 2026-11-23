import numpy  as np
a = np.array([[1,2,3],[4,5,6]]) # 创建一个二维数组
print(a)
print(a.shape)
print(a.ndim) # 维度
print(a.size) # 元素个数
print(a.dtype) # int64 元素数据类型
print(a.itemsize)   # 元素的字节大小 8 也就是说 占用8个字节
print(a.nbytes)  # 48 表示 总共占用了48个字节


######### ndarray 的创建

# array 将输入数据转换成 ndarray 会进行copy
a = np.array([1,2,3])
print(type(a))

#### asarray  将输入数据转换成 ndarray 不会进行copy
a = np.asarray([1,2,3])

print(type(a))


###### zeros() ones()  empty()  zeros_like() ones_like() empty_like()
a = np.zeros((3,4))
print(a)
a = np.empty((3,4)) # 并不保证初始化的值是多少
print(a)
arr  =  np.array([[1,2,3],[4,5,6]])
a = np.ones_like(arr)
print(a)

#### full 和 full_like
a =  np.full((3,4),5)
print(a)

a = np.full_like(arr,5)
print(a)

## arange()  返回给定范围内的等差数列  只能是一维数组
a = np.arange(2,12,2)
print(a)

# linspace() # 数组元素是 浮点数
a = np.linspace(0,10,10)
print(a)

# logspace()  数组 浮点
a = np.logspace(0,10,10)
print(a)

## 创建随机数组
arr1 = np.random.rand(3,3) # 0 -1 之间的浮点数 均匀分布
print(arr1)

arr2 = np.random.randint(1,10, size=(3,3))
print(arr2)


arr3 = np.random.uniform(1,10, size=(3,3))# 用从低位(包含)到高位(不包含)上均匀分布的随机浮点数填充。
print(arr3)


arr4 = np.random.randn(3,3) # 标准正态分布  均值为0，标准差为1
print(arr4)



