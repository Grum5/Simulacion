#!/usr/bin/env/python

import argparse 

class Aleatorios(object):
    def _init_(self, parametrot, bandera, cantidad, decimales, **kwargs):
        self.parametrot = parametrot
        self.bandera = bandera
        self.cantidad = cantidad
        self.decimales = decimales
        for key, value in kwargs.items():
            if key == "intervalo":
                valor_minimo =value[0]
                valor_maximo = value[1]
                if valor_minimo >= valor_maximo:
                    print("El intervalo no existe")
                    sys.exit() 
                self.valor_minimo = valor_minimo
                self.valor.maximo = valor_maximo

class CrearIntervalo(Aleatorios):
    def _init_(self, *args, **kwargs):
        super()._init_(args, * kwargs)

def main(**kwargs):
    # Parametro t para el generador
    parametrot = 337719
    # Se inidca con 1 si es suma o -1 si es resta
    bandera = 1
    # cantidad de aleatorios por generar
    cantidad = 5
    # Numero de decimales por redondear
    decimales = 2
    CrearIntervalo(parametrot, bandera, cantidad, decimales, **kwargs)

if __name__ == '_main_':
    parser = argparse.ArgumentParser(
        prog = 'simulacion3.py',
        formatter_class= argparse.RawDescriptionHelpFormatter, 
        description="""
        Generar valores en el intervalo [a,b] empleando el generador congruencial multipplicativo
                                x_(n+1) = (ax_n) mod (m)
        Donde: 
        a= 8t +/- 3
        m= 2 ** 31
        El usuario deberá indicar el inicio y el fin del intervalo en la forma
        simulacion3.py --intervalo a,b
        Opcionalmente, se podrán indicar la cantidad de valores aleatorios por 
        ser generados, así como la cantidad de decimales por emplear
        """,
        epilog="""
        La informacion de los resultados, se almacernará en el archivo simulacion3.csv.
        """
    )

    parser.add_argument('-i','--intervalo',
                        dest="intervalo", help="Intervalo por ser generado",
                        type=float, nargs=2, required=True)

    parser.add_argument('-t','--parametroT', default=337719,
                        dest="t", help="Parámetro del generador (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-b','--bandera', default=1, choices=[1, -1],
                        dest="b", help="Indicar como 1 si es suma, o -1 si es resta (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-n','--cantidad', default=5,
                        dest="n", help="--Cantidad (default: %(default)s)",
                        type=int, nargs='?', required=False)

    parser.add_argument('-d','--decimales', default=2,
                        dest="decimales", help="decimales por redondear (default: %(default)s)",
                        type=int, nargs='?', required=False)

parser.parse_args()
#La k es por key y la v por value en el ciclo for
datos_entrada = {k:value for k,value in vars(parser.parse_args()).items() if value is not None}
main(**datos_entrada)