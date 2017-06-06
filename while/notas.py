x =1
cont1 = 0 
cont2 = 0

while x<=10:
	nota = int(input("ingrese la nota del alumno:"))
	if nota>=7:
		cont1 =cont1+1
	else:
		if nota<=7:
			cont2 =cont2+1
	x=x+1
	print("las notas mayores son:")
	print(cont1)
	print("las notas menor son:")
	print(cont2)
