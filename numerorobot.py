import random, os

import random, os, math
    
numero = random.randint(1,100)
robot = random.randint(1,100)
user = int()

os.system("cls")

print ('''                                    NUMERO DE LA SUERTE

El juego se trata de encontrar el numero del 1 - 100. Estaras enfrentandote contra un bot que tambien jugará.

ESCOJA NIVEL

1) FACIL

2) MEDIO

3) DIFICIL

       ''')

esc = int(input("Escoja nivel: "))
os.system("cls")

if esc == 1 :

     print ('''      BIENVENIDO AL JUEGO DEL NUMERO DE LA SUERTE!

Usted esta jugando con la dificultad FACIL del robot, suerte.      

            ''')

     print ("Robot, inserta tu numero de la suerte:  ")
     print(f"Maquina: {robot}")
     user = int(input('''Usuario, inserta tu  numero de la suerte:

Usuario: '''))

     if numero > user:
             print("El numero es mas grande")

     elif numero < user:
             print("El numero es mas chico")       

     if user == numero:
             print("El USER ADIVINO EL NUMERO")

     elif robot == numero:
         print("EL ROBOT ADIVINO EL NUMERO")

     input("Inserta enter para continuar")
     os.system("cls")

     while user != numero and robot != numero:
         if robot != numero and numero > 50: 
             robot = random.randint(50,100)

         elif robot != numero and numero < 50:
             robot = random.randint(1,50)

         print ("Robot, inserta tu numero de la suerte:  ")
         print(f"Maquina: {robot}")

         user = int(input('''Usuario, inserta tu  numero de la suerte:

Usuario: '''))

         if numero > user:
             print("El numero es mas grande")

         elif numero < user:
             print("El numero es mas chico")       

         if user == numero:
             print("El USER ADIVINO EL NUMERO")

         elif robot == numero:
             print("EL ROBOT ADIVINO EL NUMERO")      

         input("Presiona enter para continuar")
         os.system("cls")         

if esc == 2:
     print ('''BIENVENIDO AL JUEGO DEL NUMERO DE LA SUERTE!

Usted esta jugando con la dificultad MEDIO del robot, suerte.      
            ''')

     print ("Robot, inserta tu numero de la suerte:  ")
     print(f"Maquina: {robot}")

     user = int(input('''Usuario, inserta tu  numero de la suerte:

Usuario: '''))

     if numero > user:
             print("El numero es mas grande")

     elif numero < user:
             print("El numero es mas chico")       

     if user == numero:
             print("El USER ADIVINO EL NUMERO")

     elif robot == numero:
         print("EL ROBOT ADIVINO EL NUMERO")

     input("Inserta enter para continuar")
     os.system("cls")

     while user != numero and robot != numero:

         if robot != numero and numero >= 1 and numero <= 25: 
             robot = random.randint(1,25)

         elif robot != numero and numero >= 26 and numero <= 50:
             robot = random.randint(26,50)

         elif robot != numero and numero >= 51 and numero <= 75:
             robot = random.randint(51,75)

         elif robot != numero and numero >= 76 and numero <=100:
             robot = random.randint(76,100)

         print ("Robot, inserta tu numero de la suerte:  ")
         print(f"Maquina: {robot}")
         user = int(input('''Usuario, inserta tu  numero de la suerte:

Usuario: '''))

         if numero > user:
             print("El numero es mas grande")

         elif numero < user:
             print("El numero es mas chico")       

         if user == numero:
             print("El USER ADIVINO EL NUMERO")

         elif robot == numero:
             print("EL ROBOT ADIVINO EL NUMERO")

         input("Presione enter para continuar ")
         os.system("cls")

if esc == 3:

     print (''' BIENVENIDO AL JUEGO DEL NUMERO DE LA SUERTE!

Usted esta jugando con la dificultad DIFICIL del robot, suerte.      

            ''')

     print ("Robot, inserta tu numero de la suerte:  ")
     print(f"Maquina: {robot}")

     user = int(input('''Usuario, inserta tu  numero de la suerte:

Usuario: '''))

     if numero > user:
             print("El numero es mas grande")

     elif numero < user:
             print("El numero es mas chico")       

     if user == numero:
             print("El USER ADIVINO EL NUMERO")

     elif robot == numero:
         print("EL ROBOT ADIVINO EL NUMERO")

     input("Inserta enter para continuar")

     os.system("cls")

     while user != numero and robot != numero:
         if robot != numero and numero >= 1 and numero <= 10: 
             robot = random.randint(1,10)

         elif robot != numero and numero >= 11 and numero <= 20:
             robot = random.randint(11,20)

         elif robot != numero and numero >= 21 and numero <= 30:
             robot = random.randint(21,30)

         elif robot != numero and numero >= 31 and numero <= 40:
             robot = random.randint(31,40)     

         elif robot != numero and numero >= 41 and numero <= 50:
             robot = random.randint(41,50)

         elif robot != numero and numero >= 51 and numero <= 60:
             robot = random.randint(51,60)

         elif robot != numero and numero >= 61 and numero <= 70:
             robot = random.randint(61,70)

         elif robot != numero and numero >= 71 and numero <= 80:
             robot = random.randint(71,80)

         elif robot != numero and numero >= 81 and numero <= 90:
             robot = random.randint(81,90)

         elif robot != numero and numero >= 91 and numero <=100:
             robot = random.randint(91,100)

         print ("Robot, inserta tu numero de la suerte:  ")
         print(f"Maquina: {robot}")
         user = int(input('''Usuario, inserta tu  numero de la suerte:
Usuario: '''))

         if numero > user:
             print("El numero es mas grande")

         elif numero < user:
             print("El numero es mas chico")       

         if user == numero:            
             print("El USER ADIVINO EL NUMERO")
             
         elif robot == numero:
             print("EL ROBOT ADIVINO EL NUMERO")
             
         input("Inserta enter para continuar")
         os.system("cls")