# 1
lista = [1, 2, 3, 5, 7, 11, 13, 17, 23, 29]

# 2
for i, elemento in enumerate(lista):
    print(f'Elemento #{i+1}:', elemento)

# 3
lista[2] = int(input('Modifica el #3 elemento <<< '))

# 4
objetivo = int(input('Ingresa un número para buscarlo: '))
for i, elemento in enumerate(lista):
    if elemento == objetivo:
        print(f'El elemento si esta en la lista, exactamente es el elemento #{i+1}')
        break
else:
    print('El elemento no existe :(')