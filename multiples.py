import string

from typing import Iterable

#Leeme
#El problema se puede modelar como una compuerta OR
#si es multiple de 3 y multiplo de 5 --> Liniano --> 1 1 --> 1
#si es multiplo de 3 y no de 5 --> Linio --> 1 0 --> 1
#si es multiplo de 5 y no de 3 --> TI --> 0 1 --> 1

def multiple(n: int, numbers: Iterable[int]):

    # Array con los mensajes
    array = []
    array.append("Liniano")
    array.append("Linio")
    array.append("TI")

    arrayret = []


    for i in range(1, n+1):

        # Preguntamos si es Multiplo y lo guardamos como bool
        rx = multipleSimple(i, numbers[0])
        ry = multipleSimple(i, numbers[1])

        # Convertimos a string el bool para concatenarlo
        rb = str(int(rx))
        rb += str(int(ry))

        # Luego lo llevamos a entero para buscar en el array de strings (donde estan  los mensajes)
        ri = int(rb)

        # como ri esta en "Binario" 10 = 2
        if ri == 10: #Un solo If xD
            ri = 2

        # si sale del indice imprime un numero
        try:
            # Mostramos el mensaje
            print(array[ri])
            arrayret.append(array[ri])
        except IndexError:
            print(i)
    return len(arrayret)


def multipleSimple(i: int, number: int) -> bool:
    try:
        rt = i % number
    except ZeroDivisionError:
        rt = 1;
    return rt != 0


