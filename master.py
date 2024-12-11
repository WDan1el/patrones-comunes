n = int(input("Introduce el valor de n (cantidad de números a ingresar): "))

mayor = None

for i in range(n):
    num = int(input(f"Introduce el número {i + 1}: "))
    
    if mayor is None or num > mayor:
        mayor = num

print(f"El número mayor es: {mayor}")
