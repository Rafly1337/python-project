# coded by rafly 2k24
# github : https://github.com/Rafly1337
# from to salsa bila putri M.
import turtle
from math import pi, sin, cos

def draw_heart(w, h, iteration=0):
    if iteration >= len(colors):
        return
    
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(2.5)
    a = 0
    t.up()
    t.fillcolor(colors[iteration])
    t.begin_fill()
    while a < 2 * pi:
        x = w * (16 * sin(a) ** 3)
        y = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a))
        t.goto(x, y)
        a += 0.02
        t.down()
    t.end_fill()

    draw_heart(w - 3, h - 2, iteration + 1)

    # gambar teks akakawok asu.
    if iteration == len(colors) - 1: 
        t.up()
        t.color("black")
        t.setpos(0, 0)
        t.write("ga ada ga ada.", align="center", font=("verdana", 15, "bold")) # buat ganti namanya
        t.down()

colors = ['#FF69B4', '#FFB6C1', '#FF1493'] # tambahkan warna

# set up screen / besar kecil 
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#FFB6C1")
screen.title("from diri sendiri")
draw_heart(16, 16)
turtle.done()
