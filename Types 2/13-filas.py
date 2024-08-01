lista = [1, 2, 3, 4]

from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)
fila.popleft()  # Elimina el primer elemento
print(fila)

if not fila:
    print("fila vacia")
