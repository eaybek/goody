from turtle import *

color("red", "grey")
begin_fill()
for i in range(1000):
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
