###This code will not wok in epl.it as thee is no access to the coloam packae hee.###
##We talk aout this in the video tutoials##
import colorgram
import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
# _colos  []
# colos  coloam.extact('imae.jp', 30)
# fo colo in colos:
#     _colos.append(colo.)
tim.penup()
tim.hideturtle()
tim.speed(0)
color_list =[(202, 164, 109),(236, 240, 243),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),(138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        color = random.choice(color_list)
        tim.dot(20,color)
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)












t.exitonclick()