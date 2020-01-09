from collections import namedtuple, deque
import math
import turtle as t

# width(4)
# forward(200)
# right(90)

# pencolor('red')
# forward(100)
# right(90)

# pencolor('green')
# forward(200)
# right(90)

# pencolor('blue')
# forward(100)
# right(90)

# done()

# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)

# for x in range(0, 250, 50):
#     drawStar(x, 0)
# done()

# 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# t.penup()
# t.left(90)
# t.forward(100)
# t.pendown()
# t.begin_fill()
# t.backward(100)
# t.right(90)
# t.circle(100,90)
# t.hideturtle()
# t.end_fill()
# t.done()


def drawOval(x, y):
    t.setposition(x, y)
    t.pendown()
    a = 1
    lenStep = 0.2
    angleStep = 1
    n = 360 // angleStep
    fac = 0.3
    t.rt(10)
    for i in range(n):
        x = n % 60
        stepn = lenStep
        # stepn = (1 + fac * abs(30 - x) / 30) * angleStep
        # if x <= 30:
        # else:
        #     stepn = (1 + fac * (30 - x) / 30) * angleStep

        if 0 <= i < n//4 or 2 * n//4 <= i < 3 * n//4:
            a = a+stepn
            t.lt(angleStep)  # 向左转3度
            t.fd(a)  # 向前走a的步长
        else:
            a = a-stepn
            t.lt(angleStep)
            t.fd(a)
# t.penup()
# t.seth(0)
# drawOval(0 ,0)
# t.penup()
# t.seth(0)
# drawOval(75 ,0)


# Point = namedtuple('Point', ['x', 'y'])
# L = deque()
# MAX_x = 100
# MAX_y = 50
# N = 1000
# for i in range(N):
#     p = Point(i/N * MAX_x, MAX_y * math.sin(i/N * 2 *math.pi))
#     L.append(p)
# for p in L:
#     t.goto(p.x, p.y)


t.done()
