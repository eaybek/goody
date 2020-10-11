from turtle import *

color("red", "yellow")
begin_fill()
for i in range(1000):
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
