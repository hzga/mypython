daikuanshu =float(input("请输入贷款金额："))
yuelilv = float(input("请输入月利率："))
nianxian = float(input("请输入贷款年限："))
print("等额本息：")
yuegong = daikuanshu*yuelilv/(1-(1/((1+yuelilv)**(nianxian*12))))
zonghuankuan=yuegong*nianxian*12
print("月供：",yuegong,"总还款：",zonghuankuan)
