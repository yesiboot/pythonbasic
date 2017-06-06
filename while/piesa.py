cantidad = 0
x = 1
n=int(input("ingrese la cantidad de piesas a procesar:"))
while x<=n:
	largo=float(input("ingrese la medidad de piesa:"))
	if largo>=1.2 and largo<=1.3:
			cantidad = cantidad+1
	x = x+1
	print("la cantidad de piesas aptas son:")
	print(cantidad)