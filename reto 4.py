rutinacontable= [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
    ]
from functools import reduce
def ordenes(rutinaContable):
    suma=list(map(lambda x:[x[0]] + list(map(lambda y:y[1]*y[2], x[1:] )) ,rutinacontable))
    suma1=list(map(lambda x:[x[0]] + [reduce(lambda y,z,:round(y+z,2), x[1:])], suma))
    suma3=list(map(lambda x:x if x[1] >= 600000 else (x[0], x[1]+25000),suma1))
    print('----------------- Inicio Registro diario --------------------------')
    for x in range(len(suma3)):
        print(f'La factura {suma3[x][0]} tiene un total en pesos de {suma3[x][1]:,.2f}')
    print('----------------- Fin Registro diario -----------------------------')

  


