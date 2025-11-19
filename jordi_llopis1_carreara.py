#########################
#Apellidos: Llopis Godino
#Nombre: Jordi
#18/11/2025

import random
import time

ronda = 0

distancia_total = 100
distancia_jugador = 0
distancia_ia = 0

combustible_jugador = 100
combustible_ia = 100

media_jugador = 0
media_ia = 0

historial = []

jugando = True
#bucle principal del juego
while True:

    #he pensat de fer un random del 0 a 100 en el de riesgo, aixina si ix un num de 0 al 10 nia fallo al normal, i si ix un num de 0 al 25 nia fallo al arriesgado
    ionico = ["seguro",5,random.randint(3,6)]
    plasma = ["normal",10,random.randint(7,12),random.randint(1,100)]
    salto_hiperespacio = ["arriesgado",25,random.randint(15,30),random.randint(1,100)]

    ronda += 1
    opcion_ia = 0

    #Si alguno llega a la meta gana
    if distancia_jugador >= distancia_total or distancia_ia >= distancia_total:
        
        print("Distancia completada")
        break
    #Si los dos se quedan sin combustible se termina el juego
    elif combustible_ia < 5 and combustible_jugador < 5:
        break
    tirada = True
    #si el jugador tiene mas de 4 de combustible puede serguir jugando, sino jugara solo la IA
    if combustible_jugador > 4:
            
        while tirada:
            opcion = int(input("Elige una opción (1 - iónico, 2 - plasma, 3 - salto hiperespacio): "))
            #Si el jugador tiene menos de 10 no podra ejecutar la 2, si el jugador tiene menos de 25 no podra ejecutar la 3 y si el jugador tiene menor distancia de 10 no podra usar el 3.
            if opcion == 1 and combustible_jugador < 5:
                print("No puedes usar esa opcion")
            elif opcion == 2 and combustible_jugador < 10:
                print("No puedes usar esa opcion")
            elif opcion == 3 and combustible_jugador < 25:
                print("No puedes usar esa opcion")
            elif opcion == 3 and distancia_jugador < 10:
                print("No puedes usar esa opcion")

            else:
                tirada = False

        if opcion == 1:
            combustible_jugador -= ionico[1]
            distancia_jugador += ionico[2]
            promedio_jugador = ionico[2]
            print("El jugador avanza {} años luz".format(promedio_jugador))

        elif opcion == 2:
            combustible_jugador -= plasma[1]
            if plasma[3] <= 10:
                promedio_jugador = 0
                print("El jugador pierde potencia y no avanza")

            else:
                distancia_jugador += plasma[2]
                promedio_jugador = plasma[2]
                print("El jugador no pierde potencia y avanza",promedio_jugador,"años luz")

        elif opcion == 3:
            combustible_jugador -= salto_hiperespacio[1]

            if salto_hiperespacio[3] <= 25:
                distancia_jugador -= 10
                promedio_jugador = 0
                print("El jugador pierde potencia y retrocede 10 años luz")
            else:
                distancia_jugador += salto_hiperespacio[2]
                promedio_jugador = salto_hiperespacio[2]
                print("El jugador no pierde potencia y avanza ",promedio_jugador,"años luz")

        #sumamos lo que avanza el jugador en cada tirada, para posteriormente dividirlo entre las rondas totales
        media_jugador += promedio_jugador
        
   #IA si la IA tiene mas de 4 de gasolina puede jugar
    if combustible_ia > 4:

        #Si la IA va detras del jugador i tiene mas de 9 de gasolina puede jugar la 2 opcion
        if distancia_ia < distancia_jugador and combustible_ia > 9:
            opcion_ia = 2
            combustible_ia -= plasma[1]
            if plasma[3] <= 10:
                promedio_ia = 0
                print("La IA pierde potencia y no avanza")
            else:
                distancia_ia += plasma[2]
                promedio_ia = plasma[2]
                print("La IA no pierde potencia y avanza",promedio_ia,"años luz")

        #La IA al ir por delante del jugador o tener menos de 9 de gasolina juega la opcion 1    
        else:
            opcion_ia = 1
            combustible_ia -= ionico[1]
            distancia_ia += ionico[2]
            promedio_ia = ionico[2]
            print("La IA avanza",promedio_ia,"años luz")
        media_ia += promedio_ia
    historial.append([ronda,distancia_jugador,distancia_ia,combustible_jugador,combustible_ia])
    print(
    
"""
****************
*** Turno {} ***
****************
        Distancia (años luz):
            {} Jugador
            {} IA
        
        Combustible (litros):
            {} Jugador
            {} IA

        Promedio (años luz por turno):
            {} Jugador
            {} IA\n""".format(ronda,distancia_jugador,distancia_ia,combustible_jugador,combustible_ia,round(media_jugador/ronda,2),round(media_ia/ronda,2)))
    

#Solo gana el jugador si tiene mas distancia que 100 y mas distancia que la IA
if distancia_jugador >= distancia_total and distancia_jugador > distancia_ia:
    print("Has ganado!!")

#La IA igual, debe tener mas de 100 de distancia y mas distancia que el jugador
elif distancia_ia >= distancia_total and distancia_ia > distancia_jugador:
    print("Has perdido!!")

#Si ninguno llega a 100 pierden los dos
else:
    print("Habeis perdido los dos!!")

time.sleep(3)

for i in range(len(historial)):
    print(
"""
Turno {}
    Jugador {} | IA {}
    Litros - Jugador {} | IA {}
""".format(historial[i][0],historial[i][1],historial[i][2],historial[i][3],historial[i][4],)
    )
print("\nGame over!")