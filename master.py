n = int(input("Introduce el valor de n: "))

S1 = sum(range(1, n + 1))


S2 = n * (n + 1) // 2


print(f"S1 (con suma de los primeros n números naturales) es: {S1}")
print(f"S2 (con la fórmula n*(n+1)/2) es: {S2}")


if S1 == S2:
    print("S1 y S2 son iguales.")
else:
    print("S1 y S2 no son iguales.")
#em pese a aser los otors proyectos por mi cuenta#