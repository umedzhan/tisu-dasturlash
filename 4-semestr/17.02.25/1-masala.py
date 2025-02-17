import turtle as t

def stars(n):
	for i in range(5):
		t.forward(n)
		t.right(144)

t.speed(2)

t.fillcolor('red')
t.begin_fill()

t.forward(400)
t.left(90)

t.forward(7)
t.left(90)

t.forward(400)
t.left(90)

t.forward(7)

t.end_fill()

#oq
t.forward(50)
t.left(90)

t.forward(400)
t.left(90)

t.forward(50)
t.left(180)
t.forward(50)

t.fillcolor('red')
t.begin_fill()

t.forward(7)
t.right(90)

t.forward(400)
t.right(90)

t.forward(7)
t.right(180)

t.end_fill()

t.forward(7)

#yashil
t.fillcolor('green')
t.begin_fill()
t.forward(50)

t.left(90)
t.forward(400)

t.left(90)
t.forward(50)
t.end_fill()

t.forward(64)

t.fillcolor('blue')
t.begin_fill()



t.forward(50)
t.left(90)



t.forward(400)
t.left(90)

t.forward(50)


t.end_fill()

t.up()
t.goto(25, 32)
t.down()

t.fillcolor('white')
t.begin_fill()

t.circle(20)

t.up()
t.goto(35, 32)
t.down()

t.circle(20)

t.up()
t.goto(50, 32)
t.down()
t.end_fill()

t.fillcolor('blue')
t.begin_fill()

t.color('blue')

t.forward(25)
t.left(90)

t.forward(30)
t.left(90)

t.forward(50)
t.left(90)

t.forward(30)
t.left(90)

t.forward(40)

t.end_fill()

#yulduzlari

t.up()
t.goto(60, 50)

t.fillcolor('white')
t.begin_fill()
stars(10)

t.up()
t.goto(70, 50)
# t.down()

stars(10)

t.up()
t.goto(80, 50)
# t.down()

stars(10)

t.end_fill()


t.up()
t.goto(60, 40)

t.fillcolor('white')
t.begin_fill()
stars(10)

t.up()
t.goto(70, 40)

stars(10)

t.up()
t.goto(80, 40)

stars(10)

t.up()
t.goto(90, 40)

stars(10)

t.end_fill()

# t.down()

stars(10)

t.up()
t.goto(60, 30)

t.fillcolor('white')
t.begin_fill()
stars(10)

t.up()
t.goto(70, 30)

stars(10)

t.up()
t.goto(80, 30)

stars(10)

t.up()
t.goto(90, 30)

stars(10)

t.up()
t.goto(100, 30)

stars(10)

t.end_fill()



# t.hideturtle()
t.done()
