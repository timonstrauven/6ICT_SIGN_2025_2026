import adafruit_dht #importeert module adafruit_dht
import board #importeert de module board
from gpiozero import RGBLED#importeert rgbled uit module gpiozero
dhtDevice = adafruit_dht.DHT11(board.D18) #variabele dhtDevice --> DHT11 op pin D18
led_kleur = [[255,0,0] , [205,38,38] , [205,55,0] , [250,128,114] , [238,149,114] , [255,127,0] , [205,133,0] , [238,221,130] , [238,221,130] , [205,205,0] , [255,246,143] , [124,252,0] , [0,255,0] , [78,238,148] , [0,245,255] , [151,255,255] , [0,255,255] , [135,206,250] , [0,191,255] , [30,144,255] , [0,0,255] ]#lijst van alle waarden voor de rgbled
rgb_led = RGBLED(red= 14, green=15, blue=16)#variabele rgbled met aan iedere kleur een pin


while True:#while loop
    temperature_c = dhtDevice.temperature# temperatuur gemeten door DHT11 in graden celsius
    tempdht11 = temperature_c # variabele tempdht11 met waarde de gemeten temperatuur door dht11
    omzetten = int(tempdht11//2)#variabele omzetten met als waarde de uitkomst van de deling
    rgb_led(led_kleur[omzetten][0], [omzetten][1], [omzetten][2])#variabele rgb_led met per kleur een waarde van variabele omzetten 
