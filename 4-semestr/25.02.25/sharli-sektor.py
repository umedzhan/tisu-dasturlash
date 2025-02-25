import turtle as t
import math

t.speed(0)

a = 200
b = 40

t.dot()
t.forward(200)
t.left(90)
for i in range(361):  # 0 dan 180 gacha - yarim ellips
    angle = math.radians(i)  # Darajani radianga aylantirish
    x = a * math.cos(angle)  # X koordinatasi
    y = b * math.sin(angle)  # Y koordinatasi
    t.goto(x, y)

t.left(90)
t.forward(400)

b = 110
for i in range(181):  # 0 dan 180 gacha - yarim ellips
    angle = math.radians(i)  # Darajani radianga aylantirish
    x = a * math.cos(angle)  # X koordinatasi
    y = b * math.sin(angle)  # Y koordinatasi
    t.goto(x, y)
    if i == 90:
    	t.dot()

t.left(135)
t.forward(284)
t.dot()

t.left(90)
t.forward(284)

t.goto(0, 0)
t.left(45)
t.forward(110)

t.up()
t.goto(-20, 40)
t.write("H", font=("Times New Roman", 20, "normal"))

t.goto(130, -100)
t.write("R", font=("Times New Roman", 20, "normal"))

t.mainloop()