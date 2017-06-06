numero1 = int(input("ingrese un numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercer numero:"))
if numero1 > numero2:
	print(numero1)
else:
	if numero1>numero3:
		print(numero1)
	else:
		if numero2 > numero3:
			print(numero2)
		else:
			print(numero3)