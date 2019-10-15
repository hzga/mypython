import turtle

turtle.goto(200,0)
turtle.goto(200,200)
turtle.goto(0,200)
turtle.goto(0,0)  # 绘制一个正方形

turtle.penup()
turtle.goto(100,100)
turtle.pendown()  # 将指针跳到这个位置（100,100）

turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
turtle.goto(100,100)  # 绘制另一个正方形

turtle.goto(200,200)  # 连接两个正方形

turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(200,0)  # 绘制斜边

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.goto(0,0)  # 绘制斜边

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(0,200)  # 绘制斜边

turtle.done()
