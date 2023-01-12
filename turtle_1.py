from turtle import *
import colorsys

bgcolor('black')
speed(0)
pensize(1)

hue = 0.009

for i in range(250):
	color = colorsys.hsv_to_rgb(hue,0.6,0.7)
	pencolor(color)
	hue+=0.008
	right(i)
	circle(150,i)
	forward(i)
	left(91)
	hue+=0.002
	
done()
