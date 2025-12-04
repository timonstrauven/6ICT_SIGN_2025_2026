from gpiozero import MCP3008 #opent de module mcp3008 van gpiozero
from signal import pause #opent de functie pause van module signal
import adafruit_dht #import de library adafruit_dht
import board #import de module board
import time #import module time
from gpiozero import LED # import LED van module gpiozero
dhtDevice = adafruit_dht.DHT11(board.D18) #variabele dhtDevice --> DHT11 op pin D18
led_oranje = LED(3) #variabele led_oranje op pin 3
led_groen = LED(27)  #variabele led_groen op pin 27
led_rood = LED(17)  #variabele led_rood op pin 17




f = open("data.DHT11_and_temp36.csv" , "w") #opent het csv bestand zodat je data kunt wegschrijven naar het bestand
f.write("datum, tijd, DHT11(°C), TMP36(°C), verschilwaarde(°C) \n") #schrijft de gegeven data over naar het csv bestand
def convert_temp(gen):
    for value in gen:
        yield(value * 3.3 - 0.5) * 100


adc = MCP3008(channel=0)

#for temp in convert_temp(adc.values):

while True:
    pause(5)
    temperature_c = dhtDevice.temperature
    huidige_tijd = time.ctime()# variabele huidige_tijd = de huidige tijd gehaald uit module time
    delen = huidige_tijd.split()# splitst de huidige tijd in delen
    jaartal_weghalen = ' '.join(delen[0:4]) # haalt het jaartal uit de gekregen data
    delen2 = jaartal_weghalen.split()# splitst jaartal_weghalen in delen
    datum = ' '.join(delen2[0:3]) # haalt de tijd uit de data zodat alleen de datum geprint wordt
    delen3 = jaartal_weghalen.split()# splitst jaartal_weghalen
    tijd = ' '.join(delen3[3:4])# haalt de datum uit de data zodat alleen de tijd geprint wordt
    for temp in convert_temp(adc.values):
        if temp > temperature_c:
            grootste_waarde = temp
            kleinste_waarde = temperature_c
        elif temperature_c > temp:
            grootste_waarde = temperature_c
            kleinste_waarde = temp

    verschilwaarde = grootste_waarde - kleinste_waarde

    if verschilwaarde > 2:
        led_oranje = 1
    elif verschilwaarde <= 2:
        led_groen = 1
    else:
        led_rood = 1

    f.write(f"{datum},{tijd},{temperature_c},{temp},{verschilwaarde} \n") #schrijft alle nodige variabelen over naar het bestand

    pause(5)

    










    