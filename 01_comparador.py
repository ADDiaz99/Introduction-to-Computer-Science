#Comparador de edades


usuario_1 = input('Cual es el nombre del primer usuario? ')
usuario_1_edad = int(input('Cual es la edad del primer usuario?'))

usuario_2 = input('Cual es el nombre del segundo usuario? ')
usuario_2_edad = int(input('Cual es la edad del segundo usuario?'))

if usuario_1_edad > usuario_2_edad:
    print(f'{usuario_1} es mayor que {usuario_2}')
elif usuario_1_edad < usuario_2_edad:
    print(f'{usuario_2} es mayor que {usuario_1}')
else:
    print(f'{usuario_1} y {usuario_2} tienen la misma edad')

