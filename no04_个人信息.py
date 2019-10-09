# 在python中，定义变量时是不需要制定变量的类型的
# 在运行的时候 python 解释器，会根据赋值语句等号右侧的数据自动推导出变量中保存数据的准确类型。
# str 表示一个字符串类型
name = "小明"
# int 表示一个整数类型
age = 18
# bool 表示一个布尔类型
gender = True
# float 表示一个小数类型，浮点数
height = 1.75

weight = 75.0

print(name)
# 在python3中不区分int和long，只有int
chang = type(2 ** 32)
chang2 = type(2 ** 64)
print(chang,chang2)
# 数字型变量可以直接计算
i = 10
f = 10.5
b = True
print(i + f,i + b,f - b,i * b)
