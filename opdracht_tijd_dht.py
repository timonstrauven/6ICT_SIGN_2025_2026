import time 
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)
f = open("tempText.txt","w")
f.write("nr. Tijd Temp.(°C) \n")
f.close()
teller = 1

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        tijd = time.strftime("%H:%M:%S")
        f = open("tempText.txt","a")
        f.write(f"{teller} {tijd}   {temperature_c} \n")
        f.close()
        teller += 1
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2)