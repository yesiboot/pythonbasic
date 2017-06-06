cantidadpreguntas = int(input("ingrese la cantiad de preguntas realizadas:"))
preguntasconrrectas = int(input("ingrese la cantidad de preguntas conrrectas"))
porcentaje = preguntasconrrectas * 100 / cantidadpreguntas
if porcentaje >= 90:
	print("tienes el nivel maximo")
else:
	if porcentaje >= 75:
		print("medio")
	else:
		if porcentaje >=50:
			print("regular")
		else:
			if porcentaje < 50:
				print("fuera de nivel")

