# Ordenar 0 de un arreglo

lista = []
cantidad = int(input("Cuantos numeros piensa ingresar: "))

for i in range(cantidad):
    elemento = float(input(f"Ingrese elemento n°{i}: "))
    lista.append (elemento)

print (f"Arreglo A = {lista}")

for i in range(cantidad):
    if (lista[i]) == 0:
        lista.append (0)
        lista.remove (0)

print(f"En la lista habian {lista.count(0)} ceros y si se mandan al final el arreglo queda tal que: {lista}")
