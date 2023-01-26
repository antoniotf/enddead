import string
#from main import *
# Creación de lista con todos los scores ordenados de mejor a peor.
# se parte de 2.000 puntos y se restan todos los movimientos realizados por nivel, ni no se completa el juego se aplican 100 movimientos por nivel no jugado.
class Score:
    def __init__(self):
        fichero = open('score.txt', 'r')
        readthefile = fichero.readlines()
        self.lista = sorted(readthefile, reverse=True)
        print("lista ordenada:")
        print(self.lista)
    def puesto(self,puesto): #devuelve los datos del puesto indicado -- Nombre Puntos y Level
        return (self.lista[puesto].split(','))

'''

nombres =['PACO', 'PEDRO', 'JOSE', 'MARIA', 'JESUS', 'ANTONIO','RICARDO']
puntos = [1322, 23, 345,32,221,9,13]
nivelAlcanzado = [15, 12, 10,4, 16, 20, 13]

fichero = open('score.txt', 'a')
i=0
for nombre in nombres:
    punto = (str(puntos[i])).zfill(4)
    nivel = nivelAlcanzado[i]
    i=i+1
    fichero.writelines(str(punto)+','+nombre+','+str(nivel)+','+'\n')
fichero.close()
'''
#

class Registrar_Score:
    def __init__(self):
        global miScore
        self.letras = list(string.ascii_uppercase)
        self.letras.insert(14, 'Ñ')
        self.letras.append('_')
        self.letras.append('del')
        self.letras.append('end')
        pass
    def entrada(self,puntos,nivel):
        global diana
        nuevaEntrada = (str(puntos).zfill(4) + ',' + '__________' + ',' + str(nivel) + ',' + '\n')
        miScore.lista.append(nuevaEntrada)
        miScore.lista.sort(reverse=True)
        print(" lista despues de nueva entrada:")
        print(miScore.lista)
        wn.bgcolor('black')
        wn.bgpic('nopic')
        wn.reset()
        lapiz.hideturtle()
        ponPersonaje.hideturtle()
        lapiz.penup()
        lapiz.speed(99)
        lapiz.color('#00ff00')
        y = 300
        x = -200
        lapiz.goto(x - 50, y)
        lapiz.write("BIENVENIDO A LA FAMA !!!!!!",
                    False, "left", ("Courier", 28, "bold"))
        lapiz.goto(x, y - 100)
        lapiz.write("A B C D E F G H I J",
                    False, "left", ("Courier", 28, "bold"))
        lapiz.goto(x, y - 150)
        lapiz.write("K L M N Ñ O P Q R S",
                    False, "left", ("Courier", 28, "bold"))
        lapiz.goto(x, y - 200)
        lapiz.write("T U V W X Y Z .",
                    False, "left", ("Courier", 28, "bold"))
        lapiz.goto(x + 350, y - 190)
        lapiz.write("_",
                    False, "left", ("Courier", 28, "bold"))
        lapiz.goto(x + 377, y - 188)
        lapiz.write("   Del   End",
                    False, "left", ("Courier", 8, "bold"))
        # lapiz.write("puntos totales ={}".format(puntos), False, "left", ("Courier", 18, "bold"))
        diana = turtle.Turtle()
        diana.shape('sprites/CursorDiana.gif')
        diana.goto(-190, 220)
        diana.showturtle()
        diana.penup()
        diana.speed(0)
        imprime_top_5(25)  # pasar coordenada Y para la altura en la que comienza a imrimir la tabla de scores.
        activar_teclas('highscore')
        while True:
            wn.update()
            wn.tracer(0)
            pass






# TODO
'''
Para la clase registar_score

'''





