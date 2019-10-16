import turtle

# 绘制奥运五环
turtle.color("blue")
turtle.circle(100)  # 半径100

turtle.penup()  # 笔抬起
turtle.goto(-200,0)  # 移动到位置
turtle.pendown()  # 笔放下
turtle.color("red")
turtle.circle(100)  # 半径100

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)  # 半径100

turtle.penup()
turtle.goto(-100,-172.75)
turtle.pendown()
turtle.color("black")
turtle.circle(100)  # 半径100

turtle.penup()
turtle.goto(100,-172.75)
turtle.pendown()
turtle.color("green")
turtle.circle(100)  # 半径100

turtle.done()  # 程序继续运行
