import time #importeert de module time
from w1thermsensor import W1ThermSensor #importeert w1thermsensor van w1thermsensor
import adafruit_dht #importeert library adafruit_dht
import board #importeert de module board
dhtDevice = adafruit_dht.DHT11(board.D18) #variabele dhtDevice --> DHT11 op pin D18
 

sensor = W1ThermSensor() #variabele sensor met DS18B20 als sensor
f = open("data.csv","w") #opent het csv bestand zodat je data kunt wegschrijven naar het bestand
f.write("datum,tijd,DHT11,DS18B20,gemiddelde temp \n") #schrijft de gegeven data over naar het csv bestand
while True: #while loop
    huidige_tijd = time.ctime()# variabele huidige_tijd = de huidige tijd gehaald uit module time
    delen = huidige_tijd.split()# splitst de huidige tijd in delen
    jaartal_weghalen = ' '.join(delen[0:4]) # haalt het jaartal uit de gekregen data
    delen2 = jaartal_weghalen.split()# splitst jaartal_weghalen in delen
    datum = ' '.join(delen2[0:3]) # haalt de tijd uit de data zodat alleen de datum geprint wordt
    delen3 = jaartal_weghalen.split()# splitst jaartal_weghalen
    tijd = ' '.join(delen3[3:4])# haalt de datum uit de data zodat alleen de tijd geprint wordt
    
    

    tempds18 = temperature_in_celsius = sensor.get_temperature()# temperatuur gemeten door DS18B20 in graden celsius
    

    temperature_c = dhtDevice.temperature# temperatuur gemeten door DHT11 in graden celsius
    tempdht11 = temperature_c # variabele tempdht11 met waarde de gemeten temperatuur door dht11
    gemiddelde_temp = temperature_c + temperature_in_celsius // 2 #gemiddelde temperatuur van de twee sensoren in een geheel getal
    f.write(f"{datum},{tijd},{temperature_c},{temperature_in_celsius},{gemiddelde_temp} \n") #schrijft alle nodige variabelen over naar het bestand
    time.sleep(1.0) #wacht een seconde

