numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercer numero:"))
if numero1 > numero2 and numero1 > numero3:
	print("primer numero es mayor")
	print(numero1)
else:
	if numero2 > numero3:
		print("el segundo numero es mayor")
		print(numero2)
	else:
		print("el tercer numero es mayor")
		print(numero3)