n=int(input("Introduzca el número de valores de 'n': "))
primero=0
segundo=1
suma=0
contador=1
print("Secuencia de Fibonacci: ")
while (contador<=n):
    print(suma)
    contador+=1
    primero=segundo
    segundo=suma
    suma=primero+segundo

    
