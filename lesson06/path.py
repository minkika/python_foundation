import turtle

def move (color, width, instance):
    turtle.reset()
    turtle.home()
    turtle.width(width)
    turtle.color(color)
    turtle.down()
    turtle.left(25)
    turtle.forward(100)
    turtle.left(155)
    turtle.forward(100)
    turtle.right(155)
    turtle.forward(100)
    turtle.right(205)
    turtle.forward(100)
    turtle.write(f'I am a {instance}', True, align="center", font=("Arial", 16, "normal"))
    turtle.up()
    turtle.mainloop()