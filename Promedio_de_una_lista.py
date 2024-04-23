# Promedio de una lista

suma = 0
a = 0
lista = []
cantidad = int(input("Cuantos numeros va a ingresar: "))

for i in range(cantidad):
    a = float(input("Ingrese un numero: "))
    suma += a
    promedio = suma / cantidad
    lista.append(a)
        

print(f"El promedio de la lista {lista} es {promedio}")

