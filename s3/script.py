from clases import Persona, Espacio
from utils import comprobar_si_coinciden
import time

pepe = Persona("Pepe",2007,["Ing. Matemática"])
ana = Persona("Ana",2005,["Ing. Matemática"],velocidad=2)

espacio1 = Espacio("UAX BT502",(20,6))

while True:
    #representamos el paso de tiempo con steps
    pepe.mover()
    ana.mover()
    if comprobar_si_coinciden(pepe, ana):
        print(f"{pepe.nombre} y {ana.nombre} se pelean a muerte por si espacio en {espacio1.name}")
    print(pepe)
    print(ana)


    time.sleep(1)