x = 1
suma = 0
n = int(input("ingrese la cantidad de alturas:"))
while x<=n:
	altura =float(input("ingrese la altura:"))
	suma = suma+altura
	x = x+1
promedio = suma/n
print("la altura promedio es:")
print(promedio)
