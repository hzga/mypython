import time
print(time.time())
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
mytimes=int(time.time())
print("从1970年至今过去了",mytimes,"秒")
resec=int(mytimes)%60 #剩余秒数
days=int(int(mytimes)-resec)//3600//24
hours=int((int(mytimes)-resec)//3600-days*24)
min=int(int(mytimes)-resec)/60
mins=int(min-days*24*60-hours*60)
sec=int(mytimes-mins*60-hours*3600-days*24*3600)
print(days,hours,mins,sec)
