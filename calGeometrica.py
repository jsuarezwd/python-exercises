# 1. Triangulo
# 2. Cuadrado
# 3. Circulo

# Variable para obtener la opcion
opc = int(input("Elija el numero de la forma que quiere calcular: \n 1. Triangulo \n 2. Cuadrado \n 3. Circulo \n"))

# Evaluamos la opcion  seleccionada para entrar al bloque correspondiente
if opc == 1:
    altura = int(input('Ingrese la altura: '))
    base = int(input('Ingrese la base: '))
    area = (altura*base)/2
    print('El area del triangulo es: '+ str(area))
elif opc == 2:
    lado = int(input('Ingrese la longitud de un lado: '))
    area = lado**2
    print("El area del cuadrado es: "+ str(area))
else:
    radio = int(input("Ingrese el diametro del circulo: "))**2
    area = float(3.14)*radio
    print("El area del circulo es: "+str(area))
