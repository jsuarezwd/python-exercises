i = 0 # Contador
c = 0 # Control para saber por cuanto se va a dividir para sacar el promedio
edadtotal = 0 # Acumulador de edad
promedio = 0 # Resultado del promedio
while i < 5:
    edad = int(input("Ingrese la edad: ")) 
    sexo = str(input("Ingrese el sexo M o F: ")) 
    if(sexo == 'F' and edad > 17): 
        c += 1
        edadtotal+=edad     
    i+=1
promedio = edadtotal/c
print("El promedio es: "+str(promedio))
