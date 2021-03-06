'''
定义一个学生类，用来形容学生
'''


# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingyue = Student()


# 在定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意：
    # 1. def doHomework 的缩进层级
    # 2。系统默认有一个self参数
    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用retun语句
        return


# 实例化一个叫yueyeu的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.course)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()


class A():
    name = "dana"
    age = 18

    def say(self):
        self.name = "aaaa"
        self.age = 200


# 此时，A称为类实例
print(A.name)
print(A.age)

print('*' * 20)
print(id(A.name))
print(id(A.age))

print('*' * 20)
# 此时，a称为对象实例
a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
