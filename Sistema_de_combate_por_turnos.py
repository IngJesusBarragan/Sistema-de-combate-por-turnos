import random
import time

# Declaro variables
Personaje_Protagonista = "Infernape"
Personaje_Rival = "Pikachu"
# Puntos de vida (HP)
vida_jugador = 100
vida_rival = 100
# Curaciones
Pociones = 4
Pociones_Rival = 4

print("¡Hola! Te acabas de encontrar a Pikachu. Usa a tu Infernape para vencerlo.")
print("\n¡Prepárate para derrotarlo!")

# Los Bucles
time.sleep(2)
while vida_jugador > 0 and vida_rival > 0:
    print(f"\n{Personaje_Protagonista}: {vida_jugador} HP | {Personaje_Rival}: {vida_rival} HP")  
    Turno_Completado = False
    while not Turno_Completado:
        time.sleep(1)
        print("\nMovimientos de Infernape: ")  
        print("1. Supergolpe")
        print("2. Lanzallamas")
        print("3. Rueda de Fuego")
        print("4. Combate Cercano")
        print(f"5. Poción ({Pociones})")
        time.sleep(1)
        Acción = input("\nSelecciona el número del movimiento. \n¿Qué movimiento usarás?: ")
        time.sleep(1)
# Ataco al rival
        if Acción == "1":
            daño = random.randint(18, 25) 
            if random.randint(1, 100) <= 8: # 10% de probabilidad de esquivar
                print(f"\n¡{Personaje_Rival} lo esquivó! No recibió daño.")
            else:
                print(f"\n{Personaje_Protagonista} usó Supergolpe.")
                if random.randint(1, 100) <= 15: 
                    daño = daño * 2
                    print("\n¡Un golpe crítico!")
                vida_rival = vida_rival - daño
            Turno_Completado = True
        elif Acción == "2":
            daño = random.randint(14, 20) 
            if random.randint(1, 100) <= 8: # 10% de probabilidad de esquivar
                print(f"\n¡{Personaje_Rival} lo esquivó! No recibió daño.")
            else:
                print(f"\n{Personaje_Protagonista} usó Lanzallamas.")
                if random.randint(1, 100) <= 15: 
                    daño = daño * 2
                    print("\n¡Un golpe crítico!")
                vida_rival = vida_rival - daño
            Turno_Completado = True
        elif Acción == "3":
            daño = random.randint(8, 14) 
            if random.randint(1, 100) <= 8: # 10% de probabilidad de esquivar
                print(f"\n¡{Personaje_Rival} lo esquivó! No recibió daño.")
            else:
                print(f"\n{Personaje_Protagonista} usó Rueda de Fuego.")
                if random.randint(1, 100) <= 15: 
                    daño = daño * 2
                    print("\n¡Un golpe crítico!")
                vida_rival = vida_rival - daño
            Turno_Completado = True
        elif Acción == "4":
            daño = random.randint(13, 19) 
            if random.randint(1, 100) <= 8: # 10% de probabilidad de esquivar
                print(f"\n¡{Personaje_Rival} lo esquivó! No recibió daño.")
            else:
                print(f"\n{Personaje_Protagonista} usó Combate Cercano.")
                if random.randint(1, 100) <= 15: 
                    daño = daño * 2
                    print("\n¡Un golpe crítico!")
                vida_rival = vida_rival - daño
            Turno_Completado = True
        elif Acción == "5":
            if Pociones > 0:
                vida_jugador = min(100, vida_jugador + 20)
                Pociones = Pociones - 1
                print("\nHemos usado una poción.")
                print(f"Te has curado. (Te quedan {Pociones} pociones).")
                Turno_Completado = True
            else:
                print("\n¡No te quedan pociones! Elige un ataque.")
        else:
            print(f"\nOpción no válida. Por favor, elige un número del 1 al 5.")
        time.sleep(1)
    if vida_rival <= 0:
            vida_rival = 0
    print(f"\n{Personaje_Protagonista}: {vida_jugador} HP | {Personaje_Rival}: {vida_rival} HP")  
# Es el turno de atacar de Pikachu.
    if vida_rival > 0:
        time.sleep(1)
        print("\n¡Ahora es turno de Pikachu!")
        print("\nMovimientos de Pikachu: ")  
        time.sleep(1) # Son para hacer el turno un poco más lento
        print("1. Impactrueno")
        print("2. Ataque Rápido")
        print("3. Tacleada de Voltios")
        print("4. Cola de Hierro")
        print(f"5. Poción ({Pociones_Rival})")
        Pikachu_Decidido = False
        while not Pikachu_Decidido:
            time.sleep(1)
            Acción_Rival = str(random.randint(1, 5))  # Pongo a que Pikachu ataque de forma aleatoria
            if Acción_Rival == "1":
                daño_rival = random.randint(18, 25) # 1. Calculas daño base
                if random.randint(1, 100) <= 8:
                    print(f"\n¡{Personaje_Protagonista} esquivó el ataque con éxito!")
                else:
                    print("\nPikachu ha usado Impactrueno.")
                    if random.randint(1, 100) <= 15:    # 2. Check de crítico
                        daño_rival = daño_rival * 2
                        print("\n¡Pikachu ha asestado un golpe crítico!")
                    vida_jugador = vida_jugador - daño_rival
                Pikachu_Decidido = True
            elif Acción_Rival == "2":
                daño_rival = random.randint(8, 14) # 1. Calculas daño base
                if random.randint(1, 100) <= 8:
                    print(f"\n¡{Personaje_Protagonista} esquivó el ataque con éxito!")
                else:
                    print("\nPikachu ha usado Ataque Rápido.")
                    if random.randint(1, 100) <= 15:    # 2. Check de crítico
                        daño_rival = daño_rival * 2
                        print("\n¡Pikachu ha asestado un golpe crítico!")
                    vida_jugador = vida_jugador - daño_rival
                Pikachu_Decidido = True
            elif Acción_Rival == "3":
                daño_rival = random.randint(14, 20) # 1. Calculas daño base
                if random.randint(1, 100) <= 8:
                    print(f"\n¡{Personaje_Protagonista} esquivó el ataque con éxito!")
                else:
                    print("\nPikachu ha usado Tacleada de Voltios.")
                    if random.randint(1, 100) <= 15:    # 2. Check de crítico
                        daño_rival = daño_rival * 2
                        print("\n¡Pikachu ha asestado un golpe crítico!")
                    vida_jugador = vida_jugador - daño_rival
                Pikachu_Decidido = True
            elif Acción_Rival == "4":
                daño_rival = random.randint(12, 17) # 1. Calculas daño base
                if random.randint(1, 100) <= 8:
                    print(f"\n¡{Personaje_Protagonista} esquivó el ataque con éxito!")
                else:
                    print("\nPikachu ha usado Cola de Hierro.")
                    if random.randint(1, 100) <= 15:    # 2. Check de crítico
                        daño_rival = daño_rival * 2
                        print("\n¡Pikachu ha asestado un golpe crítico!")
                    vida_jugador = vida_jugador - daño_rival
                Pikachu_Decidido = True
            elif Acción_Rival == "5":
                if Pociones_Rival > 0:
                    vida_rival = min(100, vida_rival + 20)
                    Pociones_Rival = Pociones_Rival -1
                    print("\nPikachu ha usado poción.")
                    print(f"Pikachu se ha curado. (Le quedan {Pociones_Rival} pociones).")
                    Pikachu_Decidido = True
                else:
                    print("\n¡A Pikachu no le quedan pociones!")
            time.sleep(1)
        if vida_jugador <= 0:
                vida_jugador = 0
if vida_jugador > 0:
    print(f"\n¡Has derrotado a Pikachu!\n")
else:
    print(f"\n{Personaje_Protagonista}: {vida_jugador} HP | {Personaje_Rival}: {vida_rival} HP \n\n¡Has sido derrotado!\n")
    
    

        
    
        
        
        
        
        
        
        