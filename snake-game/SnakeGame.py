import turtle
import  time
import random
posponer= 0.1
#CONFIGURACION DE LA VENTANA---------------------------------------------------------------------------------

window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("grey")
window.setup(width=600,height=600)
window.tracer(0)

#CABEZA DE LA SERPIENTE-----------------------------------------------------------------------------------------

Cabeza= turtle.Turtle()
Cabeza.speed(0)
Cabeza.shape("square")
Cabeza.penup()
Cabeza.goto(0,0)
Cabeza.direction="stop"
Cabeza.color("green")

#CUERPO SERPIENTE---------------------------------------------------------------------------------------------------

segmentos=[]



#COMIDA-------------------------------------------------------------------------------------------------------------
Comida= turtle.Turtle()
Comida.speed(0)
Comida.shape("circle")
Comida.penup()
Comida.goto(0,100)
Comida.color("red")


#FUNCIONES------------------------------------------------------------------------------
def arriba():
	Cabeza.direction = "up"
def abajo():
	Cabeza.direction = "down"	
def izquierda():
	Cabeza.direction = "left"
def derecha():
	Cabeza.direction = "right"	


#CONTROLES DE TECLADO-------------------------------------------------------------------

window.listen()	
window.onkeypress(arriba,   "Up")
window.onkeypress(abajo,    "Down")
window.onkeypress(izquierda,"Left")
window.onkeypress(derecha,  "Right")





def mov():
 	
	if Cabeza.direction== "up":
		y = Cabeza.ycor()
		Cabeza.sety(y + 20)

	if Cabeza.direction== "down":
		y = Cabeza.ycor()
		Cabeza.sety(y - 20)

	if Cabeza.direction== "left":
		x = Cabeza.xcor()
		Cabeza.setx(x -20)


	if Cabeza.direction== "right":
		x = Cabeza.xcor()
		Cabeza.setx(x + 20)
	

while True:
	window.update()

	#CHOQUE BORDES--------------------------------------------------------------------------------------------------
	if Cabeza.xcor() > 280 or Cabeza.xcor() < -280 or Cabeza.ycor() > 280 or Cabeza.ycor() < -280:
		time.sleep(1)
		Cabeza.goto(0,0)
		Cabeza.direction= "stop"


		#ESCONDER LOS SEGMENTOS---------------------------------------------------------------------------------

		for segmento in segmentos:
			segmento.goto(10000,10000)

		#LIMPIAR LISTA DE SEGMENTOS--------------------------------------------------------------
		
			segmentos.clear()	




	#CHOQUE COMIDA---------------------------------------------------------------------------------------------
	if Cabeza.distance(Comida)<20:
		x=random.randint(-280,280)
		y=random.randint(-280,280)
		Comida.goto(x,y)

		nuevo_segmento= turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.direction="stop"
		nuevo_segmento.color("green")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)

	#MOVER EL CUERPO DE LA SERPIENTE-----------------------------------------------------------------------------------------
	totalSeg= len(segmentos)
	for index in range(totalSeg -1, 0,-1):
		x=segmentos[index-1].xcor()
		y=segmentos[index-1].ycor()
		segmentos[index].goto(x,y)

	if totalSeg>0:
		x=Cabeza.xcor()
		y=Cabeza.ycor()
		segmentos[0].goto(x,y)	
	mov()		

	time.sleep(posponer)
	
	