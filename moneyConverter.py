# Programa para conversion de divisas, este converira de peso domincano a dolar o euros
monto = float(input("Ingrese el valor a convertir: "))
tasa_dolares = float(47.60) 
tasa_euros = float(52.10)

total_dolares = round(monto / tasa_dolares,2) 
total_euros = round(monto / tasa_euros,2)

print("La conversion a dolares es: "+str(total_dolares))
print("La conversion a euros es: "+str(total_euros))