n = int(input("Introduce un número entero n (n ≥ 0) para calcular su factorial: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")

#como puedo utilizar el for mejor casi no lo ce utilizar#