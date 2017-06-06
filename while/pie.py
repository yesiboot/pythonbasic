cantidad = 0
x =1
n = int(input("ingrese la cantidad de piezas:"))
while x<=n:
	longitud = float(input("ingrese longitud:"))
	if longitud>=1.2 and longitud<=1.3:
		cantidad = cantidad+1
	x = x+1
print("la cantidad de piezas aptas son:")
print(cantidad)