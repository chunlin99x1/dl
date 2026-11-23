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

## arange()








