# 餐布桌布设计1  | 灰底白线
 
# 程序初始化操作
import turtle            # 导入 turtle 库
turtle.setup(800,600)    # 设置窗口的大小为 宽800*高600像素，窗口位于屏幕中心。
turtle.pensize(2)        # 设置画笔的粗细为 2
turtle.bgcolor("gray")   # 设置背景颜色为 gray
turtle.pencolor("white") # 设置画布颜色为 white
turtle.speed(0)          # 设置海龟的绘图速度为0,最快。参数为1时最慢。
 
# 海龟画横线
x=-400                   # 将 x坐标 初始化为 -400
y=300                    # 将 y坐标 初始化为 300
 
i=1
while i<=16:             # 确定循环次数 ，画【15+1】行横线
    turtle.penup()       # 画笔抬起
    turtle.goto(x,y)     # 让海龟移至坐标(-400,300),即窗口的左上角。
    turtle.pendown()     # 画笔落下
    turtle.forward(800)  # 海龟向前走800像素，画出一条800像素长的横线
    y=y-40               # 每次循环将y坐标减少40，【600/40=15】将画布上线平均分成15块。要画出16行横线
    i=i+1
 
# 让海龟头朝下，准备画竖线
turtle.right(90)
 
# 海龟画竖线
x=-400
y=300
j=1
while j<=21:             # 确定循环次数，画【20+1】列竖线
    turtle.penup()       # 画笔抬起
    turtle.goto(x,y)     # 让海龟移至坐标(-400,300),即窗口的左上角。
    turtle.pendown()     # 画笔落下
    turtle.forward(600)  # 海龟向前走600像素，画出一条600像素长的竖线
    x=x+40               # 每次循环将x坐标增加40，【800/40=20】将画布左右平均分成20块。要画出21行竖线
    j=j+1
 
turtle.hideturtle()      # 隐藏海龟