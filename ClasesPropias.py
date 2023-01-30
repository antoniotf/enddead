import string

# CONSTANTES :
ANCHO_PANTALLA = 940  # medida de la ventana se requiere numero par.
ALTO_PANTALLA = 700  # medida de la ventana se requiere numero par.
NIVEL_FINAL = 20 # Indica cual es el último nivel del juego.

# Creación de lista con todos los scores ordenados de mejor a peor.
# se parte de 2.000 puntos y se restan todos los movimientos realizados por nivel, ni no se completa el juego se aplican 100 movimientos por nivel no jugado.
class Score:
    def __init__(self):
        pass
    def puesto(self,puesto): #devuelve los datos del puesto indicado -- Nombre Puntos y Level
        return (self.lista[puesto].split(','))
    def cargar_ranking(self):
        fichero = open('score.txt', 'r')
        readthefile = fichero.readlines()
        self.lista = sorted(readthefile, reverse=True)


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
        self.letras = list(string.ascii_uppercase)
        self.letras.insert(14, 'Ñ')
        self.letras.append('_')
        self.letras.append('del')
        self.letras.append('end')
        pass






# TODO
'''
Para la clase registar_score

'''





