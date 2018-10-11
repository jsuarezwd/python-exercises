nombre = str(input('Ingrese el nombre del empleado: '))
horas = float(input('Ingrese las horas trabajadas: '))
precio_por_hora = float(input('Ingrese el precio por hora: '))
sub_total = horas*precio_por_hora
precio_horas_extras = (precio_por_hora*0.50) + precio_por_hora 
horas_extras = int()
monto_extra = int()
desc_afp = float() 
desc_ars = float() 

if horas > 44:
    sub_total = 44*precio_por_hora
    horas_extras = horas-44
    monto_extra = horas_extras*precio_horas_extras

monto_bruto = sub_total+monto_extra

desc_afp = monto_bruto*0.0287
desc_ars = monto_bruto*0.0304

monto_neto = monto_bruto-(desc_afp+desc_ars)

print("El sueldo bruto del empleado "+nombre+ " es de: "+str(monto_bruto)+" y el sueldo neto es: "+str(monto_neto) )      
# 