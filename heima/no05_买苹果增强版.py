price_str = input("苹果的单价：")
weight_str = input("苹果的重量：")
# 注意：两个字符串变量之间是不能直接用乘法的
# 将价格和重量转换为小数
price = float(price_str)
weight = float(weight_str)

money = price * weight

print(money)