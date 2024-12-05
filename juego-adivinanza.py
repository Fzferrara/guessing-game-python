import random


numero_secreto = random.randint(1,101) 
adivinado = False
cantidad_intentos = 0

print ("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cantidad_intentos <= 5:
    if  cantidad_intentos == 5:
        print("Perdiste, perdiste, no hay nadie peor que vos! Eran solo 5 intentos looser")
        break

    numero = int(input("Introduce un numero del 1 al 100: ")) 
    

    if numero == numero_secreto:
        print ("Has Ganado! Adivinaste el numero secreto")
        adivinado = True
    elif numero < numero_secreto:        
        print("El nuemero es mayor al ingresado")
    elif numero > numero_secreto:        
        print("El nuemero es menor al ingresado")
    cantidad_intentos += 1
    