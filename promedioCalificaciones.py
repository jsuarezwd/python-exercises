"""
Calcular el promedio de cuatro valores numericos los cuales deben estar comprendidos entre 0 y 100, los promedios deben ser presentados bajo las mismas condiciones que utiliza la universidad para hacer las evaluaciones.
"""

nombre = str(input("Ingrese el nombre del estudiante: "))
cal1 = int(input("Ingrese la primera calificacion: "))
cal2 = int(input("Ingrese la segunda calificacion: "))
cal3 = int(input("Ingrese la tercera calificacion: "))
cal4 = int(input("Ingrese la cuarta calificacion: "))
calificacion = str('');

# Se evalua que todas las cantidades de calificaciones, esten entre 0 y 100
    # Se suman todas las calificaciones y se dividen en cuatro para sacar el promedio
suma = cal1+cal2+cal3+cal4
promedio = suma//4
# Se evalua cual fue el promedio en base a la cantidad se asiga una valor a la variable calificacion
if promedio > 89:
    calificacion = 'A'
elif promedio > 79:
    calificacion = 'B'
elif promedio > 74:
    calificacion = 'C'
elif promedio > 69:
    calificacion = 'D'
elif promedio > 59:
    calificacion = 'FE'
elif promedio > 50:
    calificacion = 'FI'
else: 
    calificacion = 'F' 

if (promedio > 0 and promedio < 101):
    print("El promedio del estudiante "+nombre+" es: "+str(promedio)+" para una calificacion: "+str(calificacion))
else:
    print("Hay una calificacion fuera del rango permitido, por favor revise e intente nuevamente.")