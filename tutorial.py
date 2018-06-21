#Tutorial

from vpython import *

bola=sphere(pos=vector(-5,0,0), radius=0.5, color=color.red)
muroR=box(pos=vector(6,0,0), size=vector(2,12,12), color=color.green)

bola.velocity=vector(10,0,0)

deltat=0.005
t=0
bola.pos=bola.pos + bola.velocity*deltat

while t < 3:
	rate(50)
	if bola.pos.x >= muroR.pos.x:
		bola.velocity.x=-bola.velocity.x
	bola.pos=bola.pos + bola.velocity*deltat
	t=t+deltat


