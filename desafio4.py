#4- Tiempo de viaje.
# Un viajero desea saber cuánto tiempo tomó un viaje que realizó. 
#Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
minutos_totales=1
minutos=1
horas=1
while minutos_totales:
    horas =int(input("ingrese los tiempos del viaje seleccionado ( si ingresa 0 el bucle se rompe):"))
    total_minutos = 0
    minutos = int(input("Tiempo del tramo: "))
    if minutos ==0:
        break   
    total_minutos+=minutos 
    

hora_totales= minutos_totales // 60
minutos_restantes = minutos_totales  % 60
print(f"las horas {horas} serian  y los minutos {minutos} correspondientes ")