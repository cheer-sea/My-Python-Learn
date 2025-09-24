## 这个仓库用于记录python的学习历程，尝试python的一些特别东西，如类(Class)等等。
### 仓库里有两个分支，main分支里是一些py的基础知识和一些重要内容的小尝试，practice分支里是一些相关代码练习

### 一、编程实践
#### 1.1 类的小实践 (student_info.py) 
#### 1.2 类的继承算法 (my_class_inherit.py) 
#### 1.3 类的掠夺功能 (my_class_rob.py) 

### 二、总结收获
类是python中非常重要的概念，类的变量和函数对应着我们现实生活的属性和行为，通过类可以更好的组织代码，贴切现实，提高代码的可读性和可维护性。

 **student_info.py** 文件中使用了 ( inti ) 构造方法，这里用括号表示原本的双下划线。构造方法可以直接为对象的属性进行定义，如原本要定义某学生(某对象)的姓名为'Hello'，如果手写，代码如下：
 > self.name = 'Hello'

其中'self'代表当前对象，'name'代表属性名，'Hello'代表属性值。

但我们使用构造方法 ( init )的话，则可以直接在创建对象时，为对象的属性赋值，代码如下：
 > student = Student('Hello')

这样就无需再手动赋值，对象的属性会直接被初始化。

**my_class_inherit.py** 文件中展示了类的继承算法，通过继承可以让子类拥有父类的所有属性和方法，并可以对父类进行扩展。
``` 
class Phone:
    def __init__(selfprice):
        self.price = price
```
上面这段代码定义了一个类 Phone，我们打算把它作为父类
```
class MyPhone(Phone):
    def call_by_5g(self):
        print('5G call')
```
上面这段代码定义了一个子类 MyPhone,它会继承父类 Phone 的所有属性和方法，并可以扩展，这里就新定义了一个方法 call_by_5g。

假设我们已经定义了三个类， MyPhone, NFCReader, RemoteControl，我们也可以构建一个子类同时继承这三个（or可能更多）的父类，代码如下：
```
class A_Phone(Myphone, NFCReader, RemoteControl)
    pass
```
其中，pass关键字的使用有利于解决语法错误，并表明该子类还未定义任何新东西。

**torch_data_read.py** 文件中尝试了读取数据，对pytorch中的 Dataset 进行实践

**my_class_rob.py** 文件中尝试了类的掠夺功能，实质上在新定义的类中使用其他类实例化一个self的属性，从而通过这个属性，调用其他类的属性和方法。







