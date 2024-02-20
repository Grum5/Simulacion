# Generador congruencial multiplicativo
#
# Javier Osvaldo Perez Bretado
# feb 12.24
#
# al22760591@ite.edu.mx


import csv
import argparse
import sys
from enum import Enum
from libs.fun.common import validar_dato, validar_decimales
from libs.classes.Errores2 import Errores2

'''

class Errores(Enum):
    PARAMETROA = 'El valor del parametro a no puede ser negativo'
    PARAMETROB = 'El valor del parametro b no puede ser negativo'
    MODULO01 = 'El valor del modulo a no puede ser negativo'
    SEMILLA = 'El valor de la semilla a no puede ser negativo'
    CANTIDAD = 'No pueden generar una cantidad negativa de aleatorios'
    DECIMALES = 'No pueden generar una cantidad negativa de decimales'
    MODULO02 = 'El valor del modulo a no puede ser negativo'

'''


class Aleatorios(object):
    def _init_(self, parametroa, parametrob, modulo, semilla, cantidad, decimales, **kwargs):
        self.parametroa = parametroa
        self.parametrob = parametrob
        self.modulo = modulo
        self.semilla = semilla
        self.cantidad = cantidad
        self.decimales = decimales
        self.kwargs = kwargs
        for key, value in kwargs.items():
            if key == 'a':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.PARAMETROA.value)
                    sys.exit()
                self.parametroa = value
            if key == 'b':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.PARAMETROB.value)
                    sys.exit()
                self.parametrob = value
            if key == 'm':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.MODULO01.value)
                    sys.exit()
                self.modulo = value
            if key == 's':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.SEMILLA.value)
                    sys.exit()
                self.semilla = value
            if key == 'n':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.CANTIDAD.value)
                    sys.exit()
                self.cantidad = value
            if key == 'd':
                try:
                    assert (self.validar_dato(value))
                except AssertionError:
                    print(Errores2.DECIMALES.value)
                    sys.exit()
                self.decimales = value
        if self.modulo <= self.parametroa or self.modulo <= self.parametrob or self.modulo <= self.semilla:
            print(Errores2.MODULO02.value)
            sys.exit()



''' 

    @staticmethod
    def validar_dato(valor):
        return True if valor >= 0 else False

    @staticmethod
    def validar_decimales(valor):
        return True if valor >= 0 else False

'''

class GenerarAleatorios(Aleatorios):
    def _init_(self, args,*kwargs):
        super()._init_(args,*kwargs)

    def aleatorios(self):    
        pseudoaleatorios = [self.semilla]
        for i in range(1,self.cantidad + 1 ):   
            temp = (self.parametroa * pseudoaleatorios[i-1]+ self.parametroa + self.parametrob) %self.modulo
            pseudoaleatorios.append(temp)
        pseudoaleatorios.pop(0)
        Aleatorios= list(map(lambda x: x/self.modulo, pseudoaleatorios) )
        return Aleatorios

    @staticmethod
    def crear_archivo (valores):
        data = [] #arreglo en donde estara la informacion a enviar al archivo
        header = ['Num', 'Aleatorio']
        for i in range(len(valores)): 
            data.append([i+1,valores[i]])
        with open('hola.csv','w', newline='')as archivo:
            writer = csv.writer(archivo)
            writer.writerow(header)
            writer.writerows(data)
    print("El archivo ha sido creado ")
    

def main(parametroa=161419, parametrob=202549, modulo=123456789, semilla=161419,cantidad=5, decimales=2, **kwargs):
    iniciar = GenerarAleatorios(parametroa, parametrob, modulo, semilla, cantidad, decimales, **kwargs)
    aleatorios = iniciar.aleatorios()
    #for aleatorio in aleatorios: 
        #print (aleatorio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'simulacion2.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = """"
        Clase para generar valores aleatorios mediante el metodo congruencial
                            x_(n+1) = ( ax_n + b ) mod (m)
        Donde:
        a = Valor multiplicativo
        b = Termino independiente
        m = Módulo.
        A partir de la semilla X0, el sistema empleará este algoritmo para generar 
        una cantidad de valores 👎 que posteriormente, serán divididos entre el 
        módulo (m), generando asi un arreglo con valores entre [0,1]. 
        """,
        epilog=""""
        EN caso de no declarar ningún valor, el programa ya cuenta con valores
        establecidos por omición (default).
        """
    )
    parser.add_argument('-a', '--terminoA', default=161419,
                        dest = "a", help = "Valor multiplicativo (default: %(default)s)",
                        type = int, nargs = '?', required = False)
    parser.add_argument('-b', '--terminoB', default=202549,
                        dest="b", help="Termino independiente (default: %(default)s)",
                        type=int, nargs='?', required=False)
    parser.add_argument('-m', '--modulo', default=123456789,
                        dest="m", help="modulo (default: %(default)s)",
                        type=int, nargs='?', required=False)
    parser.add_argument('-s', '--seed', default=161419,
                        dest="s", help="Semilla (default: %(default)s)",
                        type=int, nargs='?', required=False)
    parser.add_argument('-n', '--cantidad', default=5,
                        dest="n", help="Cantidad de aleatorios por crear (default: %(default)s)",
                        type=int, nargs='?', required=False)
    parser.add_argument('-d', '--desimales', default=2,
                        dest="decimales", help="Decimales por redondear (default: %(default)s)",
                        type=int, nargs='?', required=False)
    datos_entrada = {k: v for k,v in vars(parser.parse_args()).items() if v is not None}
    main(**datos_entrada)