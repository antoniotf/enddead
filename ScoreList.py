# se parte de 2.000 puntos y se restan todos los movimientos realizados por nivel, ni no se completa el juego se aplican 100 movimientos por nivel no jugado.

class Score:
    prueba="ok"
    def __init__(self):
        fichero = open('score.txt', 'r')
        readthefile = fichero.readlines()
        self.lista = sorted(readthefile, reverse=True)



    def cargarLista(self):
        pass









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





