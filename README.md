# Reto-10
## Arreglos y listas
En este tema se aprenden la diferencia entre listas (grupo de elementos hetereogeneos y mutables), duplas (no son mutables) y arreglos (grupo de elementos homogeneos y mutables). Para aplicar estos nuevos conceptos
aprendidos se nos fue asignado un reto de 3 puntos, siendo así uno de los dos retos mas cortos que nos han colocado, siendo equivalente al reto 2.

Los puntos de este reto solo nos pide generar arreglos, así que no se apreciaran listas o duplas en este repo, y los temas previos que use para poder hacerlos es el ciclo *for*.

### Punto 1 / Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```py
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
```

### Punto 2 / Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
Este punto es interesante ya que, el producto punto, es un calculo que se hace entre vectores. Se toman los valores del mismo indice, se multiplican, luego se toman todos los productos y se suman, obteniendo así un valor único. El producto punto se puede obtener de dos maneras distintas: por definición o por vectores.

#### Producto punto por definición.
![image](https://github.com/JMC020406/Reto-10/assets/159207395/ef84da51-88de-4bef-8c5e-140325a2b557)

#### Producto punto por vectores.
![image](https://github.com/JMC020406/Reto-10/assets/159207395/1e760483-95fc-4e9d-89be-6e2a2d1f6a90)

Ambas refrencias fueron sacadas del sitio https://www.cuemath.com/algebra/dot-product/ y la cual voy a usar para resolver el punto es la primera: *Producto punto por definición*.
```py
A = []
B = []
elemento = int
producto_punto = 0
cantidad = int(input("Cuantos numeros va a ingresar: "))

for i in range(cantidad):
    a = float(input("Ingrese el elemento de A: "))
    A.append (a)
    
for i in range(cantidad):
    b = float(input("Ingrese el elemento de B: "))
    B.append (b)

print("______________________________________________________________")
print(f"Vector A = {A}") 
print(f"Vector B = {B}")

for i in range(cantidad):
    multi = (A[i]) * (B[i])
    producto_punto += multi

print(f"El producto punto de A x B = {producto_punto}")
```

### Punto 3 / Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```py
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
```
Este programa tanto ordena los ceros al final de la lista, como, dice cuandos ceros en total hay en esta.


