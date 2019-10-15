name = "小明"
print("我的名字叫 %s，请多多关照" % name)  # 字符串

student_no = 100
print("我的学号是 %06d" % student_no)  # 整数

price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f 元／斤，购买了 %.2f 斤，需要支付 %.2f 元" % (price,weight,money))

scale = 0.25
print("数据的比例是 %.2f%%" % (scale * 100))
