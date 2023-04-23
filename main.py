import turtle as t
from  turtle import Screen
import random
screen=Screen()
new_color=[]
tim=t.Turtle()
t.colormode(255)
# colors=colorgram.extract('image.jpg',30)
# for i in range(len(colors)):
#     r=colors[i].rgb.r
#     g=colors[i].rgb.g
#     b=colors[i].rgb.b
#     new_color.append((r,g,b))
# print(new_color)
count=0
c=0
colors=[ (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]
tim.right(90)
tim.penup()
tim.forward(300)
tim.pendown()
tim.left(90)
for i in range(100):
    tim.dot(20,random.choice(colors))
    tim.penup()
    count += 1
    tim.forward(50)
    tim.pendown()
    if(count==10):
        if(c==0):
            tim.dot(20, random.choice(colors))
            tim.left(90)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.left(90)
            count=0
            c=1
    if(count==10):
        if(c==1):
            tim.dot(20, random.choice(colors))
            tim.right(90)
            tim.penup()
            tim.forward(50)
            tim.pendown()
            tim.right(90)
            count=0
            c=0
