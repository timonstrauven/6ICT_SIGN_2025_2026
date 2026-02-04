import subprocess


import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18) 

f=open("DHT11_cloud.csv" , "w")
f.write("Temp, Humidity \n")
while True:
    try:        
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
        f.write(f"{temperature_c}, {humidity} \n")

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    subprocess.run(["/bin/bash", "/home/rpi/autopush.sh"])
  