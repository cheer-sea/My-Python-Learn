import numpy as np

## 创建数组
# 创建一个整数数组
a = np.array([1, 2, 3])
# 创建一个浮点数数组
b = np.array([1.0, 2.0, 3]) # 这里的 3 会自动变为 3.0

## 注意，整数插入浮点数数组时，整数会自动变为浮点数，反之亦然
# 整数 -> 浮点数
a = a.astype(float)
# 浮点数 -> 整数
b = b.astype(int)

## 查看数组形状
a_s = a.shape

## 变化数组维度
# 创建一维数组
c = np.array([1, 2, 3])
# 变为二维数组
c = c.reshape(1, 3) # 1行3列
# 上面这行也可以写为 c = c.reshape(1, -1) 列那里填 -1 表示自动计算
# 降维一维数组
c = c.reshape(-1) # -1 的原理同上

## 同值数组
ze = np.zeros(3) # 全 0 数组
on = np.ones(3) # 全 1 数组



