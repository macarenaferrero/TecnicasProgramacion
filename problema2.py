#Ingresar 4 valores, sumar los dos primeros, multiplicar los dos últimos. Mostrar resultados.

numeros = []
while len(numeros) < 4:
    num = input("Ingrese un número: ")
    numeros.append(num)
suma = int(numeros[0]) + int(numeros[1])
multiplicacion = int(numeros[2]) * int(numeros[3])

print("La suma de los primeros numeros es ", suma, " La multiplicacion de los últimos es ", multiplicacion)