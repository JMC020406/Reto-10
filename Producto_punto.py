# Producto punto (multiplicacion de vectores)

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





