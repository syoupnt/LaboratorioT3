# 1
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2
for f in range(3):
    for c in range(3):
        matriz[f][c] = int(input(f'Ingresa un número ({f}, {c}): '))

# 3
print('[')
for f in range(3):
    print('    [', end='')
    for c in range(3):
        print(f'{matriz[f][c]}' + (', ' if c < 2 else ''), end='')
    print(']' + (',' if f < 2 else ''))
print(']')

# 4
suma_total = 0
for f in matriz:
    for valor in f:
        suma_total += valor

print(f'La suma total es {suma_total}')