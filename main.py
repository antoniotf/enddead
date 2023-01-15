import keyboard
import turtle
import copy
import time
import random
from playsound import playsound
from TablaNiveles import *


class PonPersonaje(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('sprites/personaje.gif')
        #self.color('blue')
        self.penup()
        self.speed(0)


def configurar_ventana():
    global ponPersonaje
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('Dead End')
    anchoPantalla = 940  # medida de la ventana se requiere numero par
    altoPantalla = 700  # medida de la ventana se requiere numero par
    wn.setup(anchoPantalla, altoPantalla)
    wn.addshape('sprites/ladrillo.gif')
    wn.addshape('sprites/caja.gif')
    wn.addshape('sprites/exit.gif')
    wn.addshape('sprites/personaje.gif')
    #ponPersonaje = PonPersonaje()



def cargar_pantalla(level):
    global contadorMovimientos
    global lapiz
    global idStamps
    global gridJuego
    wn.reset()
    lapiz.hideturtle()
    lapiz.penup()
    cuentaMovimientos.hideturtle()
    cuentaMovimientos.penup()
    ponPersonaje.hideturtle()
    ponPersonaje.penup
    contadorMovimientos = 0
    lapiz.hideturtle()
    lapiz.speed("fastest")
    #wn.tracer(0, 0) #velocidad de carga de la pantalla instantanea.
    lapiz.shape('sprites/ladrillo.gif')
    lapiz.penup()
    lapiz.speed(0)
    # zona de juego (16 columnas x 11 filas de 0-15 y 0-10)
    gridJuego = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    idStamps = copy.deepcopy(gridJuego)
    caracter = 0
    playsound('sprites/meloInicio.mp3', block=False)
    for y in range(11):
        for x in range(16):
            gridJuego[y][x] = level[0][caracter]
            caracter = caracter + 1
            imprime(x,y,gridJuego[y][x])

    lapiz.color("blue")
    lapiz.hideturtle()
    lapiz.goto(-400, -330)
    lapiz.write("(R)reiniciar.", False, "left", ("Courier", 18, "bold"))
    lapiz.goto(94, -330)
    lapiz.write("(S)salir.", False, "left", ("Courier", 18, "bold"))
    lapiz.goto(-300, -300)
    lapiz.write("Nivel: {}".format(nivelActual), False, "left", ("Courier", 18, "bold"))
    lapiz.goto(+100, -300)
    lapiz.write("Movimientos:", False, "left", ("Courier", 18, "bold"))
    lapiz.goto(-400,-265)
    lapiz.pendown()
    lapiz.pensize(5)
    lapiz.goto(350, -265)
    lapiz.penup()
    lapiz.goto(-400,-260)
    lapiz.pendown()
    lapiz.color("green")
    lapiz.pensize(5)
    lapiz.goto(350, -260)





def imprime(x,y,tipo):#
    global lapiz
    global idStamps
    global ponPersonaje
    x_screen = (x * 50) - 400
    y_screen = 290 - (y * 50)
    if tipo == "X":
        lapiz.shape('sprites/ladrillo.gif')
    elif tipo == "@":
        lapiz.shape('sprites/caja.gif')
    elif tipo == "E":
        lapiz.shape('sprites/exit.gif')
    elif tipo == "P":
        ponPersonaje.penup()
        ponPersonaje.showturtle()
        ponPersonaje.goto((x*50)-400, (290-(y*50)))
    else:
        return
    lapiz.penup()
    lapiz.speed(0)
    lapiz.goto(x_screen,y_screen)
    if tipo != "P":
        idStamps[y][x] = lapiz.stamp()

def MuevePersonajeA(X_varia, Y_varia):
    global contadorMovimientos
    global gridJuego
    ponPersonaje.penup()
    coordenada_X_actual =int((ponPersonaje.xcor()+400)/50)
    coordenada_Y_actual =int((290 - ponPersonaje.ycor())/50)
    nueva_X =coordenada_X_actual + X_varia
    nueva_Y =coordenada_Y_actual + Y_varia
    estadoCasillaDestino =""
    estadoCasillaDestino = gridJuego[nueva_Y][nueva_X] # invertido Y / X
    if estadoCasillaDestino == 'E':
        gridJuego[nueva_Y][nueva_X]='*'#cambia la marca 'E'exit por * en el gridJuego
        rotulo_nivel_completado(contadorMovimientos)
    if estadoCasillaDestino ==' ':
        playsound('sprites/pasosonido.wav', block=False)
        ponPersonaje.goto((nueva_X * 50) - 400, (290 - (nueva_Y * 50)))
        gridJuego[coordenada_Y_actual][coordenada_X_actual] = " " #actualiza el estado de la casilla en el grid
        contadorMovimientos = contadorMovimientos + 1
        imprime_marcador_movimientos(contadorMovimientos)
    if estadoCasillaDestino == '@':
        #si empuja una caja, ver que hay detras.
        detrasDeCajaHay = gridJuego[nueva_Y + Y_varia][nueva_X + X_varia]
        if detrasDeCajaHay ==' ':
            #está libre así que desplazamos la caja.
            playsound('sprites/deslizacajasound.wav', block=False)
            imprime((nueva_X + X_varia), (nueva_Y + Y_varia),'@')
            x_caja_movida = nueva_X + X_varia
            y_caja_movida = nueva_Y + Y_varia
            gridJuego[y_caja_movida][x_caja_movida] = "@"  # actualiza el estado de la casilla en el grid
            #borrar caja movida
            identificador = idStamps[nueva_Y][nueva_X]
            lapiz.clearstamp(identificador)
            gridJuego[nueva_Y][nueva_X] = " "  # actualiza el estado de la casilla en el grid


def imprime_marcador_movimientos(x):
    cuentaMovimientos.penup()
    cuentaMovimientos.color("blue")
    cuentaMovimientos.hideturtle()
    cuentaMovimientos.goto(+285, -300)
    cuentaMovimientos.clear()
    cuentaMovimientos.write(x, False, "left", ("Courier", 18, "bold"))

def rotulo_nivel_completado(x):
    playsound('sprites/nivelCompletoSound.mp3', block=False)
    global nivelActual
    lapiz.penup()
    lapiz.goto(0,100)
    lapiz.color("blue")
    lapiz.shape("square")
    lapiz.shapesize(stretch_wid=12, stretch_len=18)
    lapiz.stamp()
    lapiz.goto(-100, 0)
    lapiz.color('#3c79b8')
    nivelActual = nivelActual + 1
    lapiz.write("NIVEL COMPLETADO\n\nMOVIMIENTOS {}\nPRÓXIMO NIVEL {}\n\n\n'press spacebar'".format(x, nivelActual),False,"left",("Courier", 18, "bold"))
    wn.update()
    keyboard.wait(' ')
    if nivelActual > nivelMaximo:
        juegoCompletado()
    else:
        cargar_pantalla(niveles[nivelActual])
def juegoCompletado():
    playsound('sprites/melodiaFinJuego.mp3', block=False)
    cargar_pantalla(niveles[0])
    while True: #TODO OPCIÓN DE CERRAR JUEGO UNA VEZ FINALIZADOS TODOS LOS NIVELES.
        wn.update()
        pass





# -------------------------------------------------- C O O D I G O --------------------------------------------------------------
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Dead End')
anchoPantalla = 940  # medida de la ventana se requiere numero par
altoPantalla = 700  # medida de la ventana se requiere numero par
wn.setup(anchoPantalla, altoPantalla)
wn.addshape('sprites/ladrillo.gif')
wn.addshape('sprites/caja.gif')
wn.addshape('sprites/exit.gif')
wn.addshape('sprites/personaje.gif')
ponPersonaje = PonPersonaje()


niveles.append(level_0)
niveles.append(level_1)
niveles.append(level_2)
niveles.append(level_3)
niveles.append(level_4)
nivelActual = 4#nivel de inicio
nivelMaximo = 4

configurar_ventana() # Configura color, y tamaño de ventan.

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

cuentaMovimientos = turtle.Turtle()
cuentaMovimientos.hideturtle()
cuentaMovimientos.penup()

cargar_pantalla(niveles[nivelActual])# Muestra la pantalla del nivel (0 el mas bajo)






#Eventos de teclado.

wn.listen()
wn.onkey(lambda: MuevePersonajeA(0, -1), "Up")
wn.onkey(lambda: MuevePersonajeA(0, 1), "Down")
wn.onkey(lambda: MuevePersonajeA(1, 0), "Right")
wn.onkey(lambda: MuevePersonajeA(-1, 0), "Left")
wn.onkey(lambda: cargar_pantalla(niveles[nivelActual]),"r")
wn.onkey(lambda: cargar_pantalla(niveles[nivelActual]),"R")
wn.tracer(0)




a=0
b=0
while True:
    """ale = random.randint(1,4)
    if ale == 1:
        MuevePersonajeA(0, -1)
    if ale == 2:
        MuevePersonajeA(0, 1)
    if ale == 3:
        MuevePersonajeA(1, 0)
    if ale == 4:
        MuevePersonajeA(-1, 0)
    a = a + 1

    if a > 500:
        a=0
        b=b+1
        print("candidad de partidas = ", b)
        cargar_pantalla(niveles[0]) """

    wn.update()

