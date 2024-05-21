import turtle
# raphael = turtle.Turtle()
# 
# raphael.fd(100)
# raphael.rt(45)
# raphael.fd(50)
# 

# donatello = turtle.Turtle()
# donatello.pu()
# donatello.setx(100)
# donatello.pd()
# donatello.lt(73)
# donatello.fd(200)


leonardo = turtle.Turtle()

# def draw_square(name, sidelength):
#     for i in range(4):
#         name.rt(90)
#         name.fd(sidelength)
#     window = turtle.Screen
#     window.exitonclick()
#     
# draw_square(leonardo, 200)

def triangle(t, size):
    for i in range(3):
        t.rt(120)
        t.fd(size)
    window = turtle.Screen()
    window.exitonclick()
        
triangle(leonardo, 200)