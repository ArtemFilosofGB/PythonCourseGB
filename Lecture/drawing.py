import turtle
import random

for i in range(100):
    temp = random.randint(1, 3)
    len_draw = 10+10*temp
    # if len_draw>200:
    #     len_draw=0
    turtle.forward(len_draw)
    turtle.right(15*temp)

