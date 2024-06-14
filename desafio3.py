#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero=int(input("ingrese el numero deseado:"))
for i in range(2,9):

 if numero%i==0:
  print("el numero  es primo") 
  break
 elif numero%i==1:
  print("el numero  no es primo" )
  break