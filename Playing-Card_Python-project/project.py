import turtle,random
import time as t


mytc=turtle.Turtle()
mytt=turtle.Turtle()
mywind=turtle.Screen()

def Card(xpos,ypos,color):
	mytc.up()
	mytc.setposition(xpos,ypos)
	mytc.down()
	mytc.color(color)
	mytc.begin_fill()
	for i in range(0,4):
		
		if i%2 != 0:
			mytc.fd(120)
		else:
			mytc.fd(90)
		mytc.right(90)

	mytc.up()
	mytc.end_fill()
	mytc.setposition(0,0)
	mytc.down()


def Dice_shape(xcor,ycor,sz,color):
	mytt.up()
	mytt.setposition(xcor,ycor)
	mytt.down()
	mytt.color(color)
	mytt.begin_fill()
	mytt.left(135)
	mytt.fd(sz)
	mytt.right(90)
	mytt.fd(sz)
	mytt.right(90)
	mytt.fd(sz)
	mytt.right(90)
	mytt.fd(sz)
	mytt.end_fill()
	mytt.up()
	mytt.left(135)
	mytt.setposition(0,0)

def heart_shape(xcor,ycor,sz,color):
	mytt.up()
	mytt.setposition(xcor,ycor)
	mytt.down()
	mytt.color(color)
	mytt.begin_fill()
	mytt.left(140)
	mytt.fd(sz)
	mytt.circle(-(sz/2),200)
	mytt.setheading(60)
	mytt.circle(-(sz/2),200)
	mytt.fd(sz)
	mytt.end_fill()
	mytt.up()
	mytt.left(140)
	mytt.setposition(0,0)

def spade_shape(xcor,ycor,sz):
	mytt.up()
	heart_shape(xcor,ycor,sz,"black")
	mytt.setposition(xcor-2,ycor+sz+6)
	mytt.begin_fill()
	mytt.left(90)
	mytt.fd(1)
	mytt.left(45)
	mytt.fd(sz/2)
	mytt.right(135)
	mytt.fd(sz)
	mytt.right(135)
	mytt.fd(sz/2)
	mytt.left(45)
	mytt.fd(1)
	mytt.end_fill()
	mytt.up()
	mytt.left(90)
	mytt.setposition(0,0)


def text(xcor,ycor,tx,color,sz):
	mytt.color(color)
	mytt.up()
	mytt.setposition(xcor,ycor)
	mytt.down()
	mytt.write(tx,False,"center",font=("Arial Narrow",sz,"bold"))
	mytt.up()
	mytt.setposition(0,0)

def Draw_Card(xpos,ypos,type):
	Card(xpos,ypos,"white")
	if(type=="spade"):
		txt=str(random.randint(5,10))
		text(xpos+15,ypos-30,txt,"black",18)
		text(xpos+75,ypos-120,txt,"black",18)
		for i in range(0,3):
			spade_shape(xpos+30,ypos-40-i*30,12)
			spade_shape(xpos+60,ypos-40-i*30,12)
	else:
		txt=str(random.randint(2,10))
		text(xpos+15,ypos-30,txt,"red",18)
		text(xpos+75,ypos-120,txt,"red",18)
		for i in range(0,3):
			Dice_shape(xpos+30,ypos-40-i*30,12,"red")
			Dice_shape(xpos+60,ypos-40-i*30,12,"red")

mytc.screen.bgcolor("green")
mywind.bgpic("F:\\background.gif")
mytt.speed(0)
mytc.speed(0)
text(-40,250,"Playing Card !","orange",24)
text(220,-250,"@author: Khairul Alom","red",12)
text(215,-270,"Date : 05.03.2020","red",10)
for i in range(0,7):
	if(i>3):
		Draw_Card(-600+i*100,-20,"hear")
	else:
		Draw_Card(-250+i*100,200,"spade")
		
mytt.hideturtle()
mytc.hideturtle()
t.sleep(100)
