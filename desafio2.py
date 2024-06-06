#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:=[2,4,6,8 ]

cantidad_horas=0
#procedimiento del programa 
hora_actual=int(input("ingrese la hora actual entre (0-24):"))

if hora_actual <0 or hora_actual >24:
       print("la hora actual debe estar entre 0-24 horas ")
else:
    cantidad_horas=int(input("ingrese la cantidad de horas :"))
#calculo de hora   
horas_futuras=(hora_actual+cantidad_horas) % 24
   
#resultado del proceso 
print(f"En {cantidad_horas} horas, el reloj marcará las {horas_futuras}:00 horas.")