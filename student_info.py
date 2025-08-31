'''
    这个源文件尝试了类的定义和构造方法，这个方法可以让我们在创建对象时，自动地设置对象的属性。
    我们通过录入学生信息来实验。
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = []
for i in range(3):
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    grade = input("请输入学生成绩：")
    student = Student(name, age, grade)
    students.append(student)
    print(f'第{i+1}个学生信息录入完成，其姓名：{student.name}，年龄：{student.age}，成绩：{student.grade}')

    