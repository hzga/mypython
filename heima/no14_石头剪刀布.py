import random  # 导入随机工具包，用户电脑随机出数。
# 导入工具包的语句，应放在文件的顶部，方便调用。

player = int(input("请输入你要出的拳 石头1/剪刀2/布3："))
computer = random.randint(1,3)

print("玩家选择的是 %d - 电脑出的拳是 %d" % (player,computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("哦耶，电脑弱爆了")

elif player == computer:
    print("居然是平局,真是天大的缘分啊")

else:
    print("不服气，我们决战到天明！")
