from gpiozero import Motor, Button, AngularServo# importeert motor, knop en de servomotor van module gpiozero
from time import sleep# importeert sleep van module time
import adafruit_dht #importeert library adafruit_dht
import board #importeert de module board
dhtDevice = adafruit_dht.DHT11(board.D18) #variabele dhtDevice --> DHT11 op pin D18


servo = AngularServo(17) # variabele servo op pin 17

motor = Motor(forward = 17,backward = 14,  pwm = True)# variabele motor, voorwaarts op pin 17 en achterwaarts op pin 14 met pwm
knop_plus = Button(2)# knop plus is op pin 2
knop_min = Button(3)# knop min is op pin 3
knop_enter = Button(22)# knop enter is op pin 22
motor_draaien_waarde = 0# waarde motor_draaien_waarde is 0
motor_draaien = 0# waarde motor_draaien is 0
while True:# while loop
    sleep(1)# 1 secdonde wachten
    if motor_draaien_waarde < 5:# als motor_draaien_waarde kleiner is als 5
        if knop_plus.is_active:# als knop plus is ingedrukt          
            motor_draaien_waarde += 1# motor_draaien_waarde plus 1
            print(f"Huidige stap: {motor_draaien_waarde}.")# print "huidige stap: met de huidige stap"
            sleep(1)# 1 seconde wachten
        if knop_enter.is_active:# als knop enter is ingedrukt
            print("Keuze bevestigd.")# print "keuze bevestigd"
            motor_draaien = motor_draaien_waarde / 5# motor_draaien is motor_draaien_waarde delen door 5 voor omvorming tussen 0 en 1
            sleep(1)# 1 seconde wacthen
    if motor_draaien_waarde > 1:# als motor_draaien_waarde groter is als 1
        if knop_min.is_active:# als knop min ingedrukt is     
            motor_draaien_waarde -= 1# motor_draaien_waarde min 1
            print(f"Huidige stap: {motor_draaien_waarde}.")# print "huidige stap: met de huidige stap"
            sleep(1)# 1 seconde wachten
        if knop_enter.is_active:# als knop enter is ingedrukt
            print("Keuze bevestigd.")# print "keuze bevestigd"
            motor_draaien = motor_draaien_waarde / 5# motor_draaien is motor_draaien_waarde delen door 5 voor omvorming tussen 0 en 1
            sleep(1)# 1 seconde wachten
    try:
        sleep(2) # 2 seconden wachten zodat de dht de temperatuur kan meter
        humidity = dhtDevice.humidity # temperatuur gemeten door DHT11 in graden celsius
        if humidity != None: # Als er niet geen temperatuur gemeten wordt(wel een temperatuur) dan voert hij volgende code uit
            if humidity == 40: # als de gemeten vochtigheid 40 is
                angle = 10 # is de hoek van de servomotor 10 graden
            elif humidity == 60: # anders als de gemeten vochtigheid 60 is
                angle = 45# is de hoek van de servomotor 45 graden
            elif humidity == 75: # anders als de gemeten vochtigheid 75 is  
                angle = 90 # is de hoek van de servomotor 90 graden
            elif humidity == 90: # anders als de gemeten vochtigheid 90 is
                angle = 135# is de hoek van de servomotor 135 graden
            elif humidity == 100: # anders als de gemeten vochtigheid 100 is
                angle = 170# is de hoek van de servomotor 170 graden
            servo.angle # de servomotor aansturen met de variabele angle die bepaald wordt door bovenstaande code
    except RuntimeError as error: # zorgt ervoor dat de code door blijft gaan als er een error is omdat hij anders nooit gaat werken(geldt voor het volledige blokje code)
        print(error.args[0]) 
        sleep(2.0) # 2 seconden wachten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    motor.forward(motor_draaien)# motor draait voorwaarts met waarde motor_draaien
