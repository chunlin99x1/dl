# 正则化-Regularization
"""
# 定义 是一种在训练机器学习模型的时候，防止模型过拟合 在损失函数增加一个正则化项
正则化就是给模型"立规矩"：不许为了讨好训练数据，把自己搞得太复杂。
L1 正则（Lasso）    系数的绝对值和 (\sum |w_i|)
L2 正则（Ridge 岭回归） 系数的平方和 (\sum w_i^2)

"""

import pandas as pd
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# 读取



