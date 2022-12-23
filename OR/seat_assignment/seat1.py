# 餐布桌布设计2 | 粉底白点

# 程序初始化操作
import turtle                 # 导入 turtle 库
turtle.setup(800, 800)         # 设置窗口的大小为 800*600像素，窗口位于屏幕中心
turtle.colormode(255)         # 改变颜色模式为RGB
turtle.bgcolor(255, 255, 255)   # 设置背景颜色为 255,160,180 （粉色系）
turtle.speed(0)                # 设置海龟的绘图速度为0,最快。
#turtle.delay(0)               # 海龟绘图延迟时间设置为0，绘图速度最快

x = -350                        # 将 x坐标 初始化为-330
y = 350                         # 将 y坐标 初始化为300

# 自定义函数，海龟画一行白点(1行 i 个)

seat_num = [3,4,5,6,8,9,9,9,9,9,9,9,9,9,5]
seat_assignment = [[1,1],
                    [2,1],
                    [1,3],
                    [3,2],
                    [4,3],
                    [2,3,2],
                    [3,3,1],
                    [3,1,3],
                    [2,1,2,1],
                    [3,2,2],
                    [1,3,3],
                    [2,3,2],
                    [3,3,1],
                    [1,1,2,2],
                    [2,2,3]]

row = len(seat_num)
# row =8

def draw_line(seat_assign):                        # 自定义函数（无参函数） draw_line
    turtle.penup()                      # 画笔抬起
    turtle.goto(x, y)                    # 海龟移动至坐标（x,y）    

    for i in range(len(seat_assign)):
        for j in range(seat_assign[i]):                   
            turtle.pendown()                   # 画笔落下
            turtle.dot(25, (0, 155, 255))    # 画直径为20像素的点，颜色为 255,205,203
            turtle.penup()                  # 画笔抬起
            turtle.forward(50)              # 每次循环画完一个点后，海龟前进50像素 【800/50=16】
        turtle.pendown()                   # 画笔落下
        turtle.dot(20, (255, 100, 203))    # 画直径为20像素的点，颜色为 255,205,203
        turtle.penup()                  # 画笔抬起
        turtle.forward(50)


def draw_line1(seat_num):                        # 自定义函数（无参函数） draw_line
    turtle.penup()                      # 画笔抬起
    turtle.goto(x, y)                    # 海龟移动至坐标（x,y）

    for j in range(seat_num):
        turtle.pendown()                   # 画笔落下
        turtle.dot(25, (255, 205, 203))    # 画直径为20像素的点，颜色为 255,205,203
        turtle.penup()                  # 画笔抬起
        turtle.forward(50)              # 每次循环画完一个点后，海龟前进50像素 【800/50=16】

# main

for j in range(row):               # 画【12-1】行白点
    draw_line(seat_assignment[j])             # 调用自定义函数 draw_line
    y = y-50                  # 每次循环将y坐标减少50像素，【600/50=12】

turtle.hideturtle()         # 隐藏海龟

ts = turtle.getscreen()
ts.getcanvas().postscript(file="seat.eps")
turtle.done()
