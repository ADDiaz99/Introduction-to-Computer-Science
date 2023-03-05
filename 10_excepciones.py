def divide_elementos_de_lista(lista, divisor):
    try: #Trycatch para salvaguardar el codigo de una division por 0
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista     #devuelve la lista intacta en caso de error


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
