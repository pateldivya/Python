import turtle;

def draw_shape(brad):
    brad.forward(50)
    brad.right(160)
    brad.forward(50)
    brad.right(20)
    
def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')
    
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('circle')
    brad.speed('fast')

    for i in range(1,37):
        
        draw_shape(brad)
        brad.right(5)
    brad.left(90)
    brad.forward(100)
    window.exitonclick()

draw_square()
