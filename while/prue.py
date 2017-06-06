x= 1
cantidad =  0
n =int(input("ingrese una cantidad de valores:"))
while x<=n:
	longi=float(input("ingrese la longitud del pructo:"))
	if longi >=1.2 and longi <=1.3:
			cantidad = cantidad+1
	x=x+1
	print("la cantidad de piesas aptas son:")
	print(cantidad)
