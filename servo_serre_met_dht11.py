from gpiozero import AngularServo #importeert klasse AngularServo van module gpiozero
import adafruit_dht #importeert library adafruit_dht
import board #importeert de module board
import time
dhtDevice = adafruit_dht.DHT11(board.D18) #variabele dhtDevice --> DHT11 op pin D18


servo = AngularServo(17) # variabele servo op pin 17
min_temp = 15 # minimum temperatuur is 15 graden
max_temp = 20 # maximum temperatuur is 20 graden



while True: # while loop
    try:
        time.sleep(2) # 2 seconden wachten zodat de dht de temperatuur kan meter
        temperature_c = dhtDevice.temperature # temperatuur gemeten door DHT11 in graden celsius
        if temperature_c != None: # Als er niet geen temperatuur gemeten wordt(wel een temperatuur) dan voert hij volgende code uit
            if temperature_c < min_temp: # als de gemeten temperatuur kleiner is dan de minimum temperatuur, dan:
                angle = 0 # is de hoek van de servomotor 0 graden
            elif temperature_c < max_temp: # anders als de gemeten temperatuur kleiner is dan de maximum temperatuur, dan:
                angle = (temperature_c - 14,9) * 36 # wordt de hoek voor deze temperatuur berekend door het verschil van de gemeten temperatuur en 14,9 maal 36 te doen
            else: # anders:
                angle = 180 # is de hoek van de servomotor 180 graden

            servo.angle # de servomotor aansturen met de variabele angle die bepaald wordt door bovenstaande code
    except RuntimeError as error: # zorgt ervoor dat de code door blijft gaan als er een error is omdat hij anders nooit gaat werken(geldt voor het volledige blokje code)
        print(error.args[0]) 
        time.sleep(2.0) # 2 seconden wachten
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

   