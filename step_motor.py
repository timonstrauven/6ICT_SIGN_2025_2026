import RPi.GPIO as GPIO# importeert de module rpi.gpio als gpio

from RpiMotorLib import RpiMotorLib# importeert de library van de motor

GpioPins = [18, 23, 24, 25]# de pinnen waaraan de controller is verbonden

mymotor = RpiMotorLib.BYJMotor("MyMotor", "28BYJ")# variabele voor de motor genaamd mymotor

while True: # while loop
    verplaatsing = int(input("Hoeveel mm wil je verplaatsen? ")) # vraag aan de gebruiker hoeveel mm hij wil verplaatsen, antwoord is de variabele verplaatsing

    rotaties = verplaatsing/7 # variabele rotaties met waarde verplaatsing die de gebruiker ingaf delen door mijn klasnummer(7)

    print("Aantal rotaties" , rotaties) # print het aantal rotaties voor overzicht

    mymotor.motor_run(GpioPins , .01, rotaties, False, False, "half", .05) # zorgt ervoor dat de motor de rotaties doet

    GPIO.cleanup # cleanup verwijdert de variabelen na het doen van alle rotaties zodat je de input opnieuw kan gebruiken zonder het programma terug opnieuw uit te voeren