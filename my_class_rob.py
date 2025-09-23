'''
    这个源文件, 尝试类的掠夺功能.
    实践后发现，类的掠夺实则是把一个其他类的实例赋给自己的属性，从而能调用其他类的属性和方法。这里注意，调用的桥梁为基于其他类创建的实例。
    代码实现如下文的:
      self.cnt = Calculator(num1, num2)。
'''

# 定义一个原始类，我们选择定义一个简易计算器类
class Calculator:
    '''简易计算器类'''
    def __init__(self, num1, num2):
        '''变量初始化'''
        self.num1 = num1
        self.num2 = num2

    def add(self):
        '''加法运算'''
        return self.num1 + self.num2
    
    def subtract(self):
        '''减法运算'''
        return self.num1 - self.num2
    
    def multiply(self):
        '''乘法运算'''
        return self.num1 * self.num2
    
    def divide(self):
        '''除法运算'''
        if self.num2 == 0:
            return '除数不能为0'
        else:
            return self.num1 / self.num2

# 定义一个抢夺类，它自身仅有加减法功能，然后掠夺原始类的乘除法功能
class TryCalculator:
    '''抢夺计算器类'''
    def __init__(self, num1, num2):
        '''变量初始化'''
        self.num1 = num1
        self.num2 = num2
        self.cnt = Calculator(num1, num2)

    def add(self):
        '''加法运算'''
        return self.num1 + self.num2
    
    def subtract(self):
        '''减法运算'''
        return self.num1 - self.num2

## 创建实例看掠夺效果
test = TryCalculator(10, 2)
print(test.add())
print(test.subtract())
print(test.cnt.multiply())
print(test.cnt.divide())

