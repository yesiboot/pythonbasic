x = 1
cantidad  = 0
n = int(input("ingrese la cantidad de piezas:"))
while x<=n:
	longitud = float(input("ingrese la longitud de las varillas:"))
	if longitud >= 1.2 and longitud <=1.3:
		cantidad = cantidad +1

	x=x+1

	print("la catidad de peizad aptas son:")
	print(cantidad)