import time
mytimes=time.time()
print(mytimes)
print("1970至今过去了：",int(mytimes),"秒")
# mytimes=3800
remainingseconds=int(mytimes)%60
hours=int(mytimes)//3600
remainingseconds2=((int(mytimes))-int(mytimes)//3600*3600)  # 小时后剩余多少秒
mins=(remainingseconds2-remainingseconds)//60
days=hours//24
hours=hours%24
print("1970至今过去了：",
      days,"天",
      hours,"小时",
      mins,"分钟",
      remainingseconds,"秒")

