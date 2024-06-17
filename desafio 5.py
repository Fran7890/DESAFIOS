#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
#el calendario vigente en ese año:

año_bisiesto=int(input("ingrese el año que desea saber:"))
if año_bisiesto%4==0:
   if año_bisiesto%100==0:
    if año_bisiesto%400==0:
      print(f"el año ingresado es {año_bisiesto} bisiesto")
else: 
 print(f"el año ingresado {año_bisiesto} no es bisiesto")