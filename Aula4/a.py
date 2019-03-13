import turtle
t = turtle.Pen()
turtle.bgcolor('black')
sides = 5
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for x in range(1000):
	t.pencolor(colors[x%sides])  # Alterna entre 6 cores
	t.circle(x * 3/sides + x) # Aumenta raio do desenho
	t.left(360/sides + 1) # Gira 360/sides e adiciona p/ espiral
	t.width (x*sides/200)