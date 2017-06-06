numero = int(input("ingrese un numero de hasta tres cifras:"))
if numero < 10:
	print("tiene una cifra")
else:
	if numero < 100:
		print("tiene dos cifras")
	else:
		if numero < 1000:
			print("tine tres cifras")
	