""" 
Imprimir el resultado del sueldo obtenido por un empleado de nombre, cuyo sueldo se obtiene de las horas trabajadas por el precio por hora menos un 7 por ciento de descuento.
"""
nombre = str(input('Ingrese el nombre del empleado: '))
horas = float(input('Ingrese las horas trabajadas: '))
precio_por_hora = float(input('Ingrese las horas trabajadas: '))
sub_total = horas*precio_por_hora
descuento = sub_total*0.07

sueldo = sub_total-descuento

print('El sueldo del empleado '+nombre+' es de: '+str(sueldo))