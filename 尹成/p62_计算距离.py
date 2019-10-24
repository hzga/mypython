import turtle

x1, y1 = eval(input("输入坐标1："))
x2, y2 = eval(input("输入坐标2："))

juli = ((x1-x2)**2+(y1-y2)**2)**0.5

print(x1,y1)
print(x2,y2)
print(juli)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(str(x1)+","+str(y1))
turtle.goto(x2, y2)
turtle.write(str(x2)+","+str(y2))

turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write("相距"+str(juli))

turtle.done()
