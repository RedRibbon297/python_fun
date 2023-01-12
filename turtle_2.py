from turtle import *
import colorsys

bgcolor('black')
speed(0)
pensize(1)

hue = 0.5

for i in range(300):
	color = colorsys.hsv_to_rgb(hue,0.7,0.8)
	pencolor(color)
	hue+=0.004
	right(i)
	circle(48,i+2)
	forward(i+0.5)
	left(71)
	hue-=0.001
	
	
done()
