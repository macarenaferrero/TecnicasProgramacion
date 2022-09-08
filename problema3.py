#Ingresados 4 valores, sacar el promedio. Mostrar resultado de la suma y el promedio.

numeros = []
while len(numeros) < 4:
    num = int(input("Ingrese un número: "))
    numeros.append(num)
suma = sum(numeros)
promedio = float(suma/4)
print("La suma de los numeros es ", suma, " y su promedio es ", promedio)