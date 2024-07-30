#La secuencia de Collatz de un número entero se construye de la siguiente forma:
#● si el número es par, se lo divide por dos
#● si es impar, se le multiplica tres y se le suma uno;
#Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
# Solicitar al usuario que introduzca un número entero positivo
numeros = int(input("Ingrese un número entero positivo: "))

if numeros <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    secuencia = [numeros]
    for _ in range(1000):  # Limita a 1000 iteraciones para evitar bucles infinitos
        if numeros == 1:
            break
        elif numeros % 2 == 0:
            numeros = numeros // 2
        else:
            numeros = numeros * 3 + 1
        secuencia.append(numeros)
    
    print("La secuencia de Collatz es:")
    print(secuencia)
