#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
def numero_inverso():
    # Solicita al usuario que ingrese un número de tres dígitos
    numero = int(input("Ingrese un número de tres dígitos: "))
    
    # Verifica que el número sea de tres dígitos
    if 100 <= numero <= 999:
        numero_invertido = 0
        while numero > 0:
            digito = numero % 10
            numero_invertido = numero_invertido * 10 + digito
            numero = numero // 10
        print("El número invertido es:", numero_invertido)
    else:
        print("El número ingresado no es de tres dígitos.")

# Llama a la función
numero_inverso()

       