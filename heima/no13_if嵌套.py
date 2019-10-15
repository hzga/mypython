has_ticket = True
# 在144集
knife_length = 10
# 无论多么复杂的程序，都是一小步一小步实现的。
if has_ticket:
    print("车票检车通过，准备开始安检")
    if knife_length > 20:
        print("您携带的刀太长了，有 %d 公分长！" % knife_length)
        print("不允许上车")
    else:
        print("安检已经通过，祝您旅途愉快！")
else:
    print("请先买票")
