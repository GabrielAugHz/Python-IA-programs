# -*- coding: utf-8 -*-
"""NReinas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Gopu2ATYglYIerrK26Jzl6JEh3Ze7w9
"""

#Figura de la reina en Ascii
reina = "\u2655"

#Funcion Verificar
# Verificar si la columna está disponible
def verificar (tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i][columna] == reina:
            return False 
# Verificar si la diagonal superior izquierda está disponible
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == reina:
            return False
        i -= 1
        j -= 1
  # Verificar si la diagonal superior derecha está disponible
    i, j = fila, columna
    while i >= 0 and j < n:
        if tablero[i][j] == reina:
            return False
        i -= 1
        j += 1
    return True


# Si se han colocado todas las reinas, se ha encontrado una solución 
# Uso de DFS función recursiva
def completo(tablero, fila, n):
    if fila == n:
        return True
    for columna in range(n):
        if verificar(tablero, fila, columna, n):
            tablero[fila][columna] = reina
            # Ir a la siguiente reina
            if completo(tablero, fila + 1, n):
                return True
            # Si la solución no es válida, se vuelve a la posición anterior y se intenta con la siguiente columna
            tablero[fila][columna] = 0
    return False

#Funcion Imprimir Tablero 
def imprimir_tablero(tablero, n):
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end=" ")
        print()

#Funcion N Reinas
def n_reinas(n):
    tablero = [[0] * n for _ in range(n)]
    if completo(tablero, 0, n) == False:
        print("No existe solución")
        return False
    imprimir_tablero(tablero, n)

# Parametros de Entrada
n_reinas(4)