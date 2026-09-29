lista = []

def mostrar_menu() -> str:
    print('''[1] Insertar un elemento al final
[2] Eliminar un elemento por posición
[3] Buscar un valor y mostrar su posición
[4] Mostrar la lista actualizada
[5] Salir''')
    return input('Elige una opción: ')

def insertar_elemento():
    elemento = input('Elemento a insertar: ')
    lista.append(elemento)

def eliminar_elemento():
    posicion = int(input('Posición del elemento a eliminar: '))
    lista.pop(posicion)

def buscar_elemento():
    valor = input('Valor a buscar: ')
    for i, elemento in enumerate(lista):
        if elemento == valor:
            print(f'Su posición es {i}')
            break
    else:
        print('No existe ese elemento')

def mostrar_elementos():
    print(lista)

if __name__ == '__main__':
    corriendo = True

    while corriendo:
        opcion = mostrar_menu()

        match opcion:
            case '1':
                insertar_elemento()
            case '2':
                eliminar_elemento()
            case '3':
                buscar_elemento()
            case '4':
                mostrar_elementos()
            case '5':
                corriendo = False
            case _:
                print(f'Opción invalida: {opcion}')