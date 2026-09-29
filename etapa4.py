lista = [3, 7, 1, 6, 2, 5, 4, 9, 8]

def burbuja(lista: list):
    nueva_lista = lista.copy()

    for _ in range(len(lista)):
        for i in range(len(nueva_lista) - 1):
            yo = nueva_lista[i]
            tu = nueva_lista[i+1]

            if yo > tu:
                nueva_lista[i] = tu
                nueva_lista[i+1] = yo

    return nueva_lista

def seleccion(lista: list):
    nueva_lista = lista.copy()

    for i in range(len(nueva_lista)):
        minimo_index = i
        for j in range(i+1, len(nueva_lista)):
            if nueva_lista[j] < nueva_lista[minimo_index]:
                minimo_index = j

        yo = nueva_lista[i]
        nueva_lista[i] = nueva_lista[minimo_index]
        nueva_lista[minimo_index] = yo

    return nueva_lista

print('ANTES:')
print(lista)
print('\nDESPUES:')
print('Burbuja   ->', burbuja(lista))
print('Selección ->', seleccion(lista))