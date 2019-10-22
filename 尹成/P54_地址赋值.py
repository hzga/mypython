str1 = "calc"
str2 = "calc"
print(id(str1),id(str2))  # id相同
str1 = "calc1"  #给变量赋值，实际上是传递新的常量的地址
print(id(str1),id(str2))  # id不同，面试中经常问到