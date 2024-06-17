#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
numero=int(input("ingrese el numero del triangulo:"))
for i in range(1,numero +1):
     for j in range(1,i+1):
      print(i,end="")
     print("")
#triángulo rectángulo como el de más abajo con tantos renglones como indique el usuario