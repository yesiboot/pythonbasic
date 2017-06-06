x = 1
cont1 = 0
cont2 = 0
gastos = 0
n = int (input("ingrese la cantidad de empleados:"))
while x<=n:
	sueldo = float(input("ingrese el sueldo de cada empleado:"))
	if sueldo <=300:
		cont1 = cont1+1
	else:
		cont2= cont2+1
	gastos = gastos+sueldo

	x= x+1

print("los que ganan  entre 100 y trecientos son:")
print(cont1)
print("mas de  quinientos")
print(cont2)
print("gastos en la empresa son:")
print(gastos)


