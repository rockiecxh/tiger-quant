# import time
# import turtle
# import random
#
#
# def drawsnake(rad):
#     turtle.fd(rad)
#     turtle.seth(120)
#     turtle.fd(rad)
#     turtle.seth(-120)
#     turtle.fd(rad)
#
#
# def main():
#     turtle.setup(1300, 800, 0, 0)
#     pythonsize = 60
#     turtle.pensize(1)
#     c = random.uniform(0, 1)
#     d = random.randint(0, 1)
#     e = random.randint(0, 1)
#     f = (c, d, e)
#     turtle.pencolor(f)
#     turtle.seth(0)
#     drawsnake(pythonsize * 6)
#
#
# main()
#
# time.sleep(100000)


import turtle
import math

p = turtle
p.penup()
# 以0,0为圆点求三角形角到圆心长度
start_position = math.pow(2, 1.0 / 3) / 2 * 500

p.setx(-start_position)
p.sety(-start_position)
p.down()

p.color('green')
p.pensize(1)  # 画笔的粗为10
for i in range(3):  # 循环语句，循环三次
    p.forward(500)  # 向前走100默认方向为x轴正方向
    p.left(120)  # 左转120


for i in range(1000):
    p.penup()
    p.goto(10, 10)
    p.down()
    p.dot(2, 'black')

p.done()
