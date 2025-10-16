from w1thermsensor import W1ThermSensor 
from time import sleep
from gpiozero import LED
import time
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D18) 
led1 = LED(5) # variabele led1 met waarde pin 5
led2 = LED(6) # variabele led1 met waarde pin 5
led3 = LED(13) # variabele led1 met waarde pin 5
led4 = LED(19) # variabele led1 met waarde pin 5
led5 = LED(26) # variabele led1 met waarde pin 5
led6 = LED(16) # variabele led1 met waarde pin 5
led7 = LED(20) # variabele led1 met waarde pin 5
led8 = LED(21) # variabele led1 met waarde pin 5 

sensor = W1ThermSensor()
while True:
    tempds18 = temperature_in_celsius = sensor.get_temperature()
    print(temperature_in_celsius)
    sleep(1)

    try:
        temperature_c = dhtDevice.temperature
        tempdht11 = temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_f: .1f} F / {temperature_c: .1f} C Humidity: {humidity}% ")

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)
    teller = 0
    som_temp = tempdht11 + tempds18 / 2
    if som_temp >= 0:
        led1.on()
    else:
        led1.off()
    if som_temp >= 5:
        led2.on()
    else:
        led2.off()
    if som_temp >= 10:
        led3.on()
    else:
        led3.off()    
    if som_temp >= 15:
        led4.on()
    else:
        led4.off()
    if som_temp >= 20:
        led5.on()
    else:
        led5.off()
    if som_temp >= 25:
        led6.on()
    else:
        led6.off()
    if som_temp >= 30:
        led7.on()
    else:
        led7.off()
    if som_temp >= 35:
        led8.on()
    else:
        led8.off()
   
        


