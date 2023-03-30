from collections import deque

def jarra(inicio, capacidad, fin):
    cola = deque([inicio])
    visitados = set([inicio])
    while cola:
        estado_actual = cola.popleft()
        print(estado_actual)
        if estado_actual == fin:
            return True
        for i in range(len(estado_actual)):
            for j in range(len(estado_actual)):
                if i != j:
                    nuevo_estado = list(estado_actual)
                    dif = capacidad[j] - estado_actual[j]
                    if dif >= estado_actual[i]:
                        nuevo_estado[j] += estado_actual[i]
                        nuevo_estado[i] = 0
                    else:
                        nuevo_estado[j] = capacidad[j]
                        nuevo_estado[i] -= dif
                    nuevo_estado = tuple(nuevo_estado)
                    if nuevo_estado not in visitados:
                        visitados.add(nuevo_estado)
                        cola.append(nuevo_estado)
    return False

inicio = (0, 0, 8)
capacidad = (3, 5, 8)
fin = (0, 4, 4)
print(jarra(inicio, capacidad, fin))
